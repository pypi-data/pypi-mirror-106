import json
from collections import deque
import concurrent.futures

from confluent_kafka import DeserializingConsumer, KafkaError, KafkaException
from confluent_kafka.serialization import StringDeserializer

from fintix_modelcurator.utils import *
from fintix_modelcurator.const import *
from fintix_modelcurator.phase import *
from fintix_modelcurator.trigger_type import *
from fintix_modelcurator.config import Config

_EXECUTOR = concurrent.futures.ThreadPoolExecutor(max_workers=1)


class DataCallbackHandler:
    INSTANCE = None

    def __init__(self):
        self.model = None
        self.phase = None
        self.model_name = None
        self.config = None
        self.kafka_settings = None
        self.consumer = None
        self.producer = None
        self.input_topic = None
        self.trigger_type = None
        self.trigger_interval = None
        self.trigger_unit = None
        self.stop_after_trigger = None

    def init(self,
             model=None,
             model_name=None,
             phase=None,
             data_source=None,
             input_topic=None,
             trigger_type=None,
             trigger_interval=None,
             trigger_unit=None,
             stop_after_triggers=None
            ):
        self.model = model
        self.phase = phase
        self.model_name = model_name
        self.config = Config.getInstance()
        self.kafka_settings = {
            'bootstrap.servers': f'{data_source}',
            'group.id': f'{model_name}-model-handler',
            'client.id': f'{model_name}-model-handler_client',
            'enable.auto.commit': True,
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'latest'
            },
            'key.deserializer': StringDeserializer('utf_8'),
            'value.deserializer':  StringDeserializer('utf_8'),
        }
        self.input_topic = input_topic
        self.trigger_type = trigger_type
        self.trigger_unit = trigger_unit
        if trigger_type == TIME_INTERVAL:
            self.trigger_interval = int(trigger_interval) * MILLISECOND_PER_UNIT.get(self.trigger_unit)
        if trigger_type == POINT_INTERVAL:
            self.trigger_interval = int(trigger_interval)
        self.stop_after_trigger = int(stop_after_triggers)
        self.consumer = DeserializingConsumer(self.kafka_settings)
        self.consumer.subscribe([self.input_topic])

    def should_trigger(self, data, start):
        if self.trigger_type == POINT_INTERVAL and len(data) >= self.trigger_interval:
            return True

        if self.trigger_type == TIME_INTERVAL:
            now = get_currenttime_ms()
            if (now - start) > self.trigger_interval:
                return True

        return False

    def start(self):
        data = []
        on_start_cb = None
        on_new_data_cb = None
        on_stop_cb = None
        if self.phase == TRAINING_PHASE:
            on_start_cb = self.model.onTrainingStart if hasattr(self.model, "onTrainingStart") else None
            on_new_data_cb = self.model.onNewTrainingData if hasattr(self.model, "onNewTrainingData") else None
            on_stop_cb = self.model.onTrainingStop if hasattr(self.model, "onTrainingStop") else None
        if self.phase == EVALUATION_PHASE:
            on_start_cb = self.model.onEvaluationStart if hasattr(self.model, "onEvaluationStart") else None
            on_new_data_cb = self.model.onNewEvaluationData if hasattr(self.model, "onNewEvaluationData") else None
            on_stop_cb = self.model.onEvaluationStop if hasattr(self.model, "onEvaluationStop") else None
        if self.phase == PREDICTION_PHASE:
            on_start_cb = self.model.onPredictionStart if hasattr(self.model, "onPredictionStart") else None
            on_new_data_cb = self.model.onNewPredictionData if hasattr(self.model, "onNewPredictionData") else None
            on_stop_cb = self.model.onPredictionStop if hasattr(self.model, "onPredictionStop") else None

        if on_start_cb is not None:
            on_start_cb()
        if on_new_data_cb is not None:
            try:
                self.consumer.subscribe([self.input_topic])
                start = get_currenttime_ms()
                trigger_count = 0
                while True:
                    msg = self.consumer.poll(timeout=1.0)
                    if msg is None:
                        continue
                    if msg.error():
                        if msg.error().code() == KafkaError._PARTITION_EOF:
                            logging.error(
                                '%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
                        elif msg.error():
                            raise KafkaException(msg.error())
                    else:
                        self.consumer.commit(msg)
                        data.append(json.loads(msg.value()))
                        if self.should_trigger(data, start):
                            on_new_data_cb(data)
                            data = []
                            trigger_count += 1
                            start = get_currenttime_ms()

                    if 0 < self.stop_after_trigger <= trigger_count: # stop_after_trigger < 0 means run forever
                        break
            finally:
                self.consumer.close()
        if on_stop_cb is not None:
            on_stop_cb()
        return NoResult, NoError

    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = DataCallbackHandler()
        return cls.INSTANCE

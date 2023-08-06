import json
import logging

from tensorflow.keras.callbacks import Callback

from fintix_modelcurator.settings import Settings
from fintix_modelcurator.config import *
from confluent_kafka import Producer


class FintixCallback(Callback):
    def __init__(self, model_name):
        self.model_name = model_name
        self.config = Config.getInstance()
        self.setting = Settings.getInstance().get_settings()
        self.kafka_settings = {
            'bootstrap.servers': f'{self.setting.get("data_source")}',
        }
        self.predict_output_topic = f"{model_name}_predict_result"
        self.producer = Producer(self.kafka_settings)
        super(Callback, self).__init__()

    def on_data_delivered(self, err, msg):
        if err is not None:
            logging.error('Message delivery failed: {}'.format(err))
        else:
            logging.error('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    ## Callback for training phase below ##

    def on_train_end(self, logs=None):
        self.producer.produce(
            f"fintix_model_monitoring_{self.model_name}_train_end",
            json.dumps(logs).encode('utf-8'),
            on_delivery=self.on_data_delivered)
        self.producer.flush()
        logging.info(f"Stop training; got logs: {logs}")

    def on_train_batch_end(self, batch, logs=None):
        logging.info(f"Training: end of batch {batch}; got logs {logs}")
        self.producer.produce(
            f"fintix_model_monitoring_{self.model_name}_train_batch",
            json.dumps(logs).encode('utf-8'),
            on_delivery=self.on_data_delivered)
        self.producer.flush()

    def on_epoch_end(self, epoch, logs=None):
        logging.info(f"End epoch {epoch} of training; got logs {logs}")
        self.producer.produce(
            f"fintix_model_monitoring_{self.model_name}_train_epoch",
            json.dumps(logs).encode('utf-8'),
            on_delivery=self.on_data_delivered)
        self.producer.flush()

    ## Callback for evaluation phase below ##

    def on_test_end(self, logs=None):
        logging.info(f"Stop testing; got logs {logs}")
        self.producer.produce(
            f"fintix_model_monitoring_{self.model_name}_test",
            json.dumps(logs).encode('utf-8'),
            on_delivery=self.on_data_delivered)
        self.producer.flush()

    def on_test_batch_end(self, batch, logs=None):
        logging.info(f"Evaluating: end of batch {batch}; got logs {logs}")
        self.producer.produce(
            f"fintix_model_monitoring_{self.model_name}_test_batch",
            json.dumps(logs).encode('utf-8'),
            on_delivery=self.on_data_delivered)
        self.producer.flush()

    ## Callback for prediction phase below ##

    def on_predict_end(self, logs=None):
        logging.info(f"Stop predicting; got logs {logs}")

    def on_predict_batch_end(self, batch, logs=None):
        logging.info(f"Predicting: end of batch {batch}; got logs {logs}")

    def upload_predict_result(self, data):
        self.producer.produce(self.predict_output_topic, json.dumps(data), on_delivery=self.on_data_delivered)
        self.producer.flush()

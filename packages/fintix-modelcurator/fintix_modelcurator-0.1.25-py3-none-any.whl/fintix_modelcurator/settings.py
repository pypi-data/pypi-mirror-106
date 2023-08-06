import json
from fintix_modelcurator.const import *


class Settings:
    INSTANCE = None

    def __init__(self):
        self.settings = None

    def init(self, setting_strings):
        self.settings = json.loads(setting_strings)
        return NoResult, NoError

    def get_settings(self):
        return self.settings

    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = Settings()
        return cls.INSTANCE

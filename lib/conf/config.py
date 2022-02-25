# -*- coding: utf-8 -*-
from config import custom_settings
from lib.conf import global_settings


class Setting():
    def __init__(self):
        ### 全局配置
        for key in dir(global_settings):
            if key.isupper():
                setattr(self, key, getattr(global_settings, key))
        ### 自定义配置
        for key in dir(custom_settings):
            if key.isupper():
                setattr(self, key, getattr(custom_settings, key))


settings = Setting()

# -*- coding: utf-8 -*-
from src.client import Agent, SSHSalt
from lib.conf.config import settings


def run():
    if settings.MODE == 'agent':
        obj = Agent()
    else:
        obj = SSHSalt()

    obj.collectAndPost()

# -*- coding: utf-8 -*-
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODE = 'agent'
SSH_PORT = 22
SSH_USERNAME = 'root'
SSH_PASSWORD = '123456'

DEBUG = True

# 可插拔式采集
PLUGINS_DICT = {
    'board': 'src.plugins.board.Board',
    'memory': 'src.plugins.memory.Memory',
    'disk': 'src.plugins.disk.Disk',
    'cpu': 'src.plugins.cpu.Cpu',
    'basic': 'src.plugins.basic.Basic',
    'nic': 'src.plugins.nic.Nic',
}



API_URL = 'http://127.0.0.1:8000/server/'
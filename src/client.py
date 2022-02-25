# -*- coding: utf-8 -*-

import requests
from lib.conf.config import settings
from src.plugins import PluginManager
import os


class Base():
    def post_data(self, server_info):
        requests.post(settings.API_URL, json=server_info)


class Agent(Base):
    # 收集数据并发送
    def collectAndPost(self):
        server_info = PluginManager().execute()
        hostname = server_info['basic']['data']['hostname']
        # print(hostname)
        res = open(os.path.join((settings.BASEDIR), 'config/cert'), 'r', encoding='utf8').read()

        if not res.strip():
            ### 第一次采集，将采集的hostname写入到一个文件中
            with open(os.path.join(settings.BASEDIR, 'config/cert'), 'w', encoding='utf8') as fp:
                fp.write(hostname)
        else:
            #### 第二次采集的时候， 永远以第一次文件中保存的主机名为标准
            server_info['basic']['data']['hostname'] = res
        for k, v in server_info.items():
            print(k, v)
        ### Content-Type':"application/json"
        self.post_data(server_info)


class SSHSalt(Base):
    def get_hostnames(self):
        hostnames = requests.get(settings.API_URL)
        return ['c1.host.com', 'c2.host.com']

    def run(self, hostname):
        server_info = PluginManager(hostname).execute()
        self.post_data(server_info)

    def collectAndPost(self):
        hostnames = self.get_hostnames()
        ### 单线程执行， 循环速度比较慢
        # for hostname in hostnames:
        #     server_info = PluginsManager(hostname).execute()
        #     self.post_data(server_info)

        ### 线程池的方式采集数据
        from concurrent.futures import ThreadPoolExecutor
        p = ThreadPoolExecutor(10)
        for hostname in hostnames:
            p.submit(self.run, hostname)


# 一方建树
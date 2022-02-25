# -*- coding: utf-8 -*-
import subprocess
import traceback

from lib.conf.config import settings
import importlib


# 管理插件信息的类
class PluginManager(object):

    def __init__(self, hostname=None):
        self.plugins_dict = settings.PLUGINS_DICT
        self.hostname = hostname
        self.debug = settings.DEBUG
        if settings.MODE == 'ssh':
            self.port = settings.SSH_PORT
            self.name = settings.SSH_USERNAME
            self.pwd = settings.SSH_PASSWORD

    ## 读取配置文件中的pluginsdict, 并执行对应模块中的process方法
    def execute(self):
        response = {}
        for k, v in self.plugins_dict.items():
            ret = {"status": None, 'data': None}
            try:
                """
                k: board
                v: src.plugins.board.Board
                """
                # 1.导入模块路径
                module_path, class_name = v.rsplit('.', 1)
                # 2.导入这个路径
                module_name = importlib.import_module(module_path)
                # 3.导入对应模块的类
                cls = getattr(module_name, class_name)
                # 4.执行类下面的process方法
                res = cls().process(self.__cmd_run, self.debug)
                ret['status'] = 10000
                ret['data'] = res
            except Exception as e:
                ret['status'] = 10001
                ret['data'] = "[%s] 采集 [%s] 出错，错误信息是: %s" % (self.hostname if self.hostname else "Agent", k , str(traceback.format_exc()))
            response[k] = ret
        return response

    def __cmd_run(self, cmd):
        if settings.MODE == 'agent':
            return self.__cmd_agent(cmd)
        elif settings.MODE == 'ssh':
            return self.__cmd_ssh(cmd)
        elif settings.MODE == 'salt':
            return self.__cmd_salt(cmd)
        else:
            # raise
            print("只支持的模式有: agent/ssh/salt")

    def __cmd_agent(self, cmd):
        # subprocess
        res = subprocess.getoutput(cmd)
        return res

    def __cmd_ssh(self, cmd):
        import paramiko
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许链接不再know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.hostname, port=self.port, username=self.name, password=self.pwd)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return result

    def __cmd_salt(self, cmd):
        # import salt.client
        # local = salt.client.LocalClient()
        # result = local.cmd('c2.salt.com', 'cmd.run', [cmd])
        command = "salt %s cmd.run %s" % (self.hostname, cmd)
        result = subprocess.getoutput(command)
        return result

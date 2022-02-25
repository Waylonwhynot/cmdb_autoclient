# -*- coding: utf-8 -*-
from lib.conf.config import settings
import subprocess
# from src.plugins import board, disk, memory
from src.plugins import PluginManager
from src.script import run
if __name__ == '__main__':
    run()
    # res = PluginManager().execute()
    # # res = PluginManager('10.0.0.1').execute()
    # for k, v in res.items():
    #     print(k, v)


# if __name__ == '__main__':
#     mode = settings.MODE
#
#     if mode == 'agent':
#         res = subprocess.getoutput('ifconfig')
#         ip = res[30:50]
#         print(ip)
#     elif mode == 'ssh':
#         import paramiko
#         # 创建SSH对象
#         ssh = paramiko.SSHClient()
#         # 允许链接不再know_hosts文件中的主机
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         # 连接服务器
#         ssh.connect(hostname='cl.salt.com', port=22, username='root', password='123')
#         # 执行命令
#         stdin, stdout, stderr = ssh.exec_command('ifconfig')
#         # 获取命令结果
#         result = stdout.read()
#         # 关闭连接
#         ssh.close()
#     else:
#         import salt.client
#         local = salt.client.LocalClient()
#         result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])
#         print(result)

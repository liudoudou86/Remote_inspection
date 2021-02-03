#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz


import paramiko
import sys,os

host = str(input('请输入IP地址：'))
port = str(input('请输入端口号：'))
user = str(input('请输入用户名：'))
password = str(input('请输入密码：'))


s = paramiko.SSHClient()                                 # 绑定实例
s.load_system_host_keys()                                # 加载本地HOST主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
s.connect(host,22,user,password,timeout=5)               # 连接远程主机
while True:
        cmd=input('cmd:')
        stdin,stdout,stderr = s.exec_command(cmd)        # 执行命令
        cmd_result = stdout.read(),stderr.read()         # 读取命令结果
        for line in cmd_result:
                print(line) # paramiko实例(账号密码登录执行命令)
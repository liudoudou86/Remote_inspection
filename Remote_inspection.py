#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz


import paramiko
import sys
import os
import PySimpleGUI as sg

def cmd_delete():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('rm -rf /home/backup_tiandy')
    # print(stdout.read())
    ssh.close() # 关闭连接

def cmd_create():
    ssh = paramiko.SSHClient() # 绑定实例
    ssh.load_system_host_keys() # 加载本地HOST主机文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机
    ssh.connect(host,port,user,pwd) # 连接远程主机
    stdin,stdout,stderr = ssh.exec_command('mkdir /home/backup_tiandy') # 执行命令
    # print(stdout.read())
    ssh.close() # 关闭连接

def sftp_put():
    ssh = paramiko.Transport((host,22))
    ssh.connect(username=user,password=pwd)
    sftp = paramiko.SFTPClient.from_transport(ssh) # 创建SFTP方法的会话连接
    sftp.put('D:\Coding\Script.zip','/home/backup_tiandy/Script.zip') # PUT文件至远端服务器
    ssh.close()

def cmd_execute():
    ssh = paramiko.SSHClient() # 绑定实例
    ssh.load_system_host_keys() # 加载本地HOST主机文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机
    ssh.connect(host,port,user,pwd) # 连接远程主机
    stdin,stdout,stderr = ssh.exec_command('cd /home/backup_tiandy/;unzip Script.zip')
    print(stdout.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/backup_tiandy/;sh Backup.sh')
    print(stdout.read())
    ssh.close() # 关闭连接

layout = [
    [sg.Text('请输入IP地址：',font='微软雅黑',size=(12, 1)),sg.Input(key='_HOST_')],
    [sg.Text('请输入端口号：',font='微软雅黑',size=(12, 1)),sg.InputText('22',key='_PORT_')],
    [sg.Text('请输入用户名：',font='微软雅黑',size=(12, 1)),sg.InputText('root',key='_USER_')],
    [sg.Text('请输入密码：',font='微软雅黑',size=(12, 1)),sg.Input(key='_PWD_')],
    [sg.Button('确认',key = '_CONFIRM_',font='微软雅黑', size=(10, 1)), sg.Exit('退出',key = '_EXIT_',font='微软雅黑', size=(10, 1))]
]
# 定义窗口，窗口名称
window = sg.Window('远程自动备份工具',layout,font='微软雅黑')
# 自定义窗口进行数值回显
while True:
    event,values = window.read()
    if event == '_CONFIRM_':
        host = str(values['_HOST_'])
        # print(ip)
        port = str(values['_PORT_'])
        # print(port)
        user = str(values['_USER_'])
        # print(user)
        pwd = str(values['_PWD_'])
        # print(pwd)
        cmd_delete = cmd_delete()
        cmd_create = cmd_create()
        sftp_put = sftp_put()
        cmd_execute = cmd_execute()
        sg.popup('操作已完成!',font='微软雅黑')
    elif event in ['_EXIT_',None]:
        break
    else:
        pass

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz


import os
import sys
import time

import paramiko
import PySimpleGUI as sg

# 删除历史备份文件及文件夹
def cmd_delete():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('rm -rf /home/BackupTiandy')
    stdin,stdout,stderr = ssh.exec_command('rm -rf /home/Script')
    stdin,stdout,stderr = ssh.exec_command('rm -rf /home/BackupTiandy.zip')
    print('删除历史备份文件',stderr.read())
    ssh.close() 

# 创建备份所需文件夹
def cmd_create():
    ssh = paramiko.SSHClient() # 绑定实例
    ssh.load_system_host_keys() # 加载本地HOST主机文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机
    ssh.connect(host,port,user,pwd) # 连接远程主机
    stdin,stdout,stderr = ssh.exec_command('mkdir /home/BackupTiandy') # 执行命令
    stdin,stdout,stderr = ssh.exec_command('mkdir /home/Script')
    print('创建备份文件夹',stderr.read())
    ssh.close() # 关闭连接

# 上传脚本文件至服务器
def sftp_put():
    ssh = paramiko.Transport((host,port))
    ssh.connect(username=user,password=pwd)
    sftp = paramiko.SFTPClient.from_transport(ssh) # 创建SFTP方法的会话连接
    sftp.put('D:\Remote_inspection.zip','/home/Script/Remote_inspection.zip') # PUT文件至远端服务器
    print('上传脚本文件至服务器')
    ssh.close()

# 下载备份文件到本地D盘根目录
def sftp_get():
    ssh = paramiko.Transport((host,port))
    ssh.connect(username=user,password=pwd)
    sftp = paramiko.SFTPClient.from_transport(ssh)
    sftp.get('/home/BackupTiandy.zip','D:\BackupTiandy.zip')
    print('下载备份文件至本地')
    ssh.close()

# 远程执行办案区webapps和x1备份脚本
def cmd_execute_Baq():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('chmod 777 *')
    print('脚本文件授权',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;bash -l Backup.sh 2>&1')
    print('Webapps和x1备份中...',stdout.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh BaqMysql.sh')
    print('Mysql数据库备份中...',stderr.read())
    ssh.close()

# 远程执行地图mysql数据库备份脚本
def cmd_execute_Dt():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('chmod 777 *')
    print('脚本文件授权',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh DtMysql.sh')
    print('Mysql数据库备份中...',stderr.read())
    ssh.close()

# 远程执行证据图片备份脚本
def cmd_execute_Storage():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('chmod 777 *')
    print('脚本文件授权',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh Storage.sh')
    print('证据图片备份中...',stderr.read())
    ssh.close()

# 压缩备份文件
def cmd_zip():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/;zip -r BackupTiandy.zip BackupTiandy/*')
    print('备份文件压缩中...',stderr.read())
    ssh.close()

outputwin = [ [sg.Output(size=(57,5))]]

layout = [
    [sg.Radio('办案区服务器', 'RADIO1', key='_RADIO1_', default=True), sg.Radio('地图服务器', 'RADIO1', key='_RADIO2_'), sg.Radio('存储服务器', 'RADIO1', key='_RADIO3_')],
    [sg.Text('请输入IP地址：',font='微软雅黑',size=(12, 1)),sg.Input(key='_HOST_')],
    [sg.Text('请输入端口号：',font='微软雅黑',size=(12, 1)),sg.InputText('22',key='_PORT_')],
    [sg.Text('请输入用户名：',font='微软雅黑',size=(12, 1)),sg.InputText('root',key='_USER_')],
    [sg.Text('请输入密码：',font='微软雅黑',size=(12, 1)),sg.Input(key='_PWD_',password_char='*')],
    #[sg.Frame('打印日志', layout = outputwin, font='微软雅黑')], 
    [sg.Button('确认',key = '_CONFIRM_',font='微软雅黑', size=(12, 1)), sg.Exit('退出',key = '_EXIT_',font='微软雅黑', size=(12, 1))]
]
# 定义窗口，窗口名称
window = sg.Window('远程自动备份工具',layout,font='微软雅黑')
# 自定义窗口进行数值回显
while True:
    event,values = window.read()
    if event == '_CONFIRM_':
        host = str(values['_HOST_'])
        # print(ip)
        port = int(values['_PORT_'])
        # print(port)
        user = str(values['_USER_'])
        # print(user)
        pwd = str(values['_PWD_'])
        # print(pwd)
        cmd_delete = cmd_delete()
        cmd_create = cmd_create()
        sftp_put = sftp_put()
        if values.get('_RADIO1_','True'):
            cmd_execute_Baq = cmd_execute_Baq()
        elif values.get('_RADIO2_','True'):
            cmd_execute_Dt = cmd_execute_Dt()
        elif values.get('_RADIO3_','True'):
            cmd_execute_Storage = cmd_execute_Storage()
        else:
            pass
        cmd_zip = cmd_zip()
        sftp_get = sftp_get()
        sg.popup_ok('备份文件已下载至【D:\BackupTiandy.zip】',title='备份完成',font='微软雅黑')
    elif event in ['_EXIT_',None]:
        break
    else:
        pass
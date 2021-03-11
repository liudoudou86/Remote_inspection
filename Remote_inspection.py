#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz


import os
import sys
import time
import zipfile

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
    # TODO：此处修改为脚本所在地址进行排查D:\BackupTiandy.zip
    sftp.get('/home/BackupTiandy.zip','D:\BackupTiandy.zip')
    print('下载备份文件至本地')
    ssh.close()

# 远程执行办案区webapps和x1备份脚本
def cmd_execute_Webapps():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;bash -l Backup_webapps.sh 2>&1')
    print('Webapps备份中...',stdout.read())
    ssh.close()

def cmd_execute_X1():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh Backup_x1.sh')
    print('X1备份中...',stderr.read())
    ssh.close()

def cmd_execute_Mysql():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh BaqMysql.sh')
    print('Mysql数据库备份中...',stderr.read())
    ssh.close()

def cmd_execute_License():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh Backup_license.sh')
    print('License授权文件备份中...',stderr.read())
    ssh.close()

# 远程执行物管数据库备份脚本
def cmd_execute_Wg():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh BaqMysql.sh')
    print('Mysql数据库备份中...',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh WgMysql.sh')
    print('WgMysql数据库备份中...',stderr.read())
    ssh.close()

# 远程执行物管数据库备份脚本
def cmd_execute_Ag():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh BaqMysql.sh')
    print('Mysql数据库备份中...',stderr.read())
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;sh AgMysql.sh')
    print('AgMysql数据库备份中...',stderr.read())
    ssh.close()

# 远程执行地图mysql数据库备份脚本
def cmd_execute_Dt():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,user,pwd)
    stdin,stdout,stderr = ssh.exec_command('cd /home/Script/;unzip Remote_inspection.zip')
    print('脚本文件解压缩',stderr.read())
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

# 解压缩ZIP包
zip_file = "BackupTiandy.zip"
def unzip_file():
    zip_src = zipfile.ZipFile(zip_file, 'r')
    zip_src.extractall()
    zip_src.close()


layout = [
    [sg.Radio('办案区webapps', 'RADIO1', key='_RADIO11_', default=True), sg.Radio('办案区x1', 'RADIO1', key='_RADIO12_'), sg.Radio('办案区Mysql', 'RADIO1', key='_RADIO13_'), sg.Radio('办案区license', 'RADIO1', key='_RADIO14_')],
    [sg.Radio('物管', 'RADIO1', key='_RADIO2_'), sg.Radio('案管', 'RADIO1', key='_RADIO3_'), sg.Radio('地图', 'RADIO1', key='_RADIO4_'), sg.Radio('存储', 'RADIO1', key='_RADIO5_')],
    [sg.Text('请输入IP地址：',font='微软雅黑',size=(12, 1)),sg.Input(key='_HOST_')],
    [sg.Text('请输入端口号：',font='微软雅黑',size=(12, 1)),sg.InputText('22',key='_PORT_')],
    [sg.Text('请输入用户名：',font='微软雅黑',size=(12, 1)),sg.InputText('root',key='_USER_')],
    [sg.Text('请输入密码：',font='微软雅黑',size=(12, 1)),sg.Input(key='_PWD_',password_char='*')],
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
        if values.get('_RADIO11_','True'):
            cmd_execute_Webapps = cmd_execute_Webapps()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_webapps') # 对文件夹进行重命名
        elif values.get('_RADIO12_','True'):
            cmd_execute_X1 = cmd_execute_X1()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_x1')
        elif values.get('_RADIO13_','True'):
            cmd_execute_Mysql = cmd_execute_Mysql()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_办案区mysql')
        elif values.get('_RADIO14_','True'):
            cmd_execute_License = cmd_execute_License()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_授权文件')   
        elif values.get('_RADIO2_','True'):
            cmd_execute_Wg = cmd_execute_Wg()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_物管') 
        elif values.get('_RADIO3_','True'):
            cmd_execute_Ag = cmd_execute_Ag()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_案管') 
        elif values.get('_RADIO4_','True'):
            cmd_execute_Dt = cmd_execute_Dt()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_地图') 
        elif values.get('_RADIO5_','True'):
            cmd_execute_Storage = cmd_execute_Storage()
            cmd_zip = cmd_zip()
            sftp_get = sftp_get()
            unzip_file = unzip_file()
            os.rename('BackupTiandy','BackupTiandy'+'_'+host+'_存储')
        else:
            pass
        sg.popup_ok('备份文件已下载至D盘根目录',title='备份完成',font='微软雅黑')
    elif event in ['_EXIT_',None]:
        break
    else:
        pass

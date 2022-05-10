#!/bin/bash --login

startdate=`date -d today +%Y_%m_%d_%H_%M`

function webapps_backup(){
    cd $TOMCAT_HOME
    tar -cvf webapps_backup_$startdate.tar.gz webapps/*
    mv webapps_backup_$startdate.tar.gz /home/BackupTiandy
}

function x1_backup(){
    cd /root
    tar -cvf x1_backup_$startdate.tar.gz x1/*
    mv x1_backup_$startdate.tar.gz /home/BackupTiandy
}

webapps_backup
x1_backup

exit 0
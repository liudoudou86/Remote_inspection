#!/bin/sh
# Author:lz

function webapps_backup(){
    cd $TOMCAT_HOME
    zip -r webapps_$(date +"%Y-%m-%d").zip ./webapps/*
    mv webapps_$(date +"%Y-%m-%d").zip /home/backup_tiandy
}

function x1_backup(){
    cd /root
    zip -r x1_$(date +"%Y-%m-%d").zip ./x1/*
    mv x1_$(date +"%Y-%m-%d").zip /home/backup_tiandy
}


webapps_backup
x1_backup
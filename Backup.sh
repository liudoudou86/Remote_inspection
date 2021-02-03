#!/bin/sh
# Author:lz

mkdir /home/$(date +"%Y-%m-%d")_backup
function webapps_backup(){
    thome = $TOMCAT_HOME
    echo "TOMCAT_HOME的目录是${thome}"
    cd $TOMCAT_HOME
    zip -r webapps_$(date +"%Y-%m-%d").zip ./webapps/*
    mv webapps_$(date +"%Y-%m-%d").zip /home/$(date +"%Y-%m-%d")_backup
}

function x1_backup(){
    cd /root
    zip -r x1_$(date +"%Y-%m-%d").zip ./x1/*
    mv x1_$(date +"%Y-%m-%d").zip /home/$(date +"%Y-%m-%d")_backup
}


webapps_backup
x1_backup
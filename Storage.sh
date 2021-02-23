#!/bin/bash --login
# Author:lz

startdate=`date -d today +%Y_%m_%d_%H_%M`

function storage_home(){
    cd /home/share
    tar -cvf home_share_backup_$startdate.tar.gz share/*
    mv home_share_backup_$startdate.tar.gz /home/BackupTiandy
}

function storage_mnt(){
    cd /mnt/disk0
    tar -cvf mnt_disk0_backup_$startdate.tar.gz disk0/*
    mv mnt_disk0_backup_$startdate.tar.gz /home/BackupTiandy
}


storage_home
storage_mnt

exit 0
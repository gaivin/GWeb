#!/usr/bin/env bash

time=$(date "+%Y%m%d-%H%M%S")
backup_file="../../dbbackup/DjangoDemo_db.json"
echo "Start Database Backup..."
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > ${backup_file}.${time} 
echo "Backup Completed. Please check the backup file ${backup_file}.${time}"

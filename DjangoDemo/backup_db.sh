#!/usr/bin/env bash

time=$(date "+%Y%m%d-%H%M%S")
backup_dir="/home/gaivin/dbbackup/"
backup_file=${backup_dir}${time}-DjangoDemoDB.json
echo "Start Database Backup..."
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > ${backup_file}
echo "Backup Completed. Please check the backup file ${backup_file}"

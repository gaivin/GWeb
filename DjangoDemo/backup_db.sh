#!/usr/bin/env bash

echo "Start Database Backup..."
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > ../dbbackup/DjangoDemo_db.json
echo "DB Backup Completed."

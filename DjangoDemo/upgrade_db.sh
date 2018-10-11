#!/usr/bin/env bash

echo "Start make migrations..."
python manage.py makemigrations
echo "Start migrate..."
python manage.py migrate
echo "DB upgrading completed."

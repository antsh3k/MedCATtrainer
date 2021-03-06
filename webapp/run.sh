#!/bin/sh

# Collect static files and migrate if needed
python /home/api/manage.py collectstatic --noinput
python /home/api/manage.py makemigrations --noinput
python /home/api/manage.py makemigrations api --noinput
python /home/api/manage.py migrate --noinput
python /home/api/manage.py migrate api --noinput

python /home/api/manage.py process_tasks &
uwsgi --http-timeout 360s --http :8000 --master --chdir /home/api/  --module core.wsgi

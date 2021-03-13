#!/bin/bash

python manage.py flush --no-input
python manage.py migrate

python manage.py start_tg_bot &
gunicorn --bind 0.0.0.0:8080 core.wsgi

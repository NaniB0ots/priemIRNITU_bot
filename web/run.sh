#!/bin/bash

python manage.py migrate

python manage.py start_vk_bot &
gunicorn --bind 0.0.0.0:8080 project.wsgi

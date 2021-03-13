#!/bin/bash

python manage.py start_tg_bot &
gunicorn --bind 0.0.0.0:8080 core.wsgi

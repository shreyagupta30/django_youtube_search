#!/bin/sh

python manage.py flush --no-input
python manage.py migrate
gunicorn -w 3 -b :8000 backend.config.wsgi:application

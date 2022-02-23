#!/bin/sh
fuser -k 8000/tcp
python manage.py clear_cache
python manage.py runserver

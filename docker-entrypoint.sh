#!/usr/bin/env bash

crontab ./crontab.cfg
cron
./manage.py migrate --fake-initial
./manage.py createcachetable
./manage.py loaddata initial_categories
./manage.py loaddata initial_flis_topics
./manage.py loaddata initial_themes
./manage.py collectstatic --noinput

gunicorn live_catalogue.wsgi:application --bind 0.0.0.0:8002

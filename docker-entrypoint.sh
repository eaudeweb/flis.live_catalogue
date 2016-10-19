#!/usr/bin/env bash

./manage.py migrate
./manage.py loaddata initial_categories
./manage.py loaddata initial_flis_topics
./manage.py loaddata initial_themes

gunicorn live_catalogue.wsgi:application --bind 0.0.0.0:8002

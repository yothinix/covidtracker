#!/usr/bin/env bash

cd $APPLICATION_ROOT\covidtracker/
python manage.py migrate
#python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000

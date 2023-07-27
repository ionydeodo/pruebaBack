#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r PruebaBack/requirements.txt

python manage.py makemigrations
python manage.py migrate
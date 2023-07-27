#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r PruebaBack/requirements.txt

python PruebaBack/manage.py makemigrations
python PruebaBack/manage.py migrate
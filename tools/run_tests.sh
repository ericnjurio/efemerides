#!/usr/bin/env sh

pipenv run coverage run manage.py test -v 2 apps \
&& pipenv run coverage html

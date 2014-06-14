#!/bin/bash
set -eux

../src/manage.py runserver 5000 --settings=HotPizzas.settings.base

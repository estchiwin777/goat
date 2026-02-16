#!/bin/sh
# 1. สั่ง Migrate ในคอนเทนเนอร์เดียวกันก่อนเริ่มแอป
python manage.py migrate --noinput
# 2. เริ่มรัน Gunicorn
gunicorn --bind 0.0.0.0:8080 --timeout 60 mysite.wsgi:application
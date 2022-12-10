# Django Document Management System

A simple document management system written in Python/Django. I run it on my Raspberry Pi 4 on my home network.

## Run on Boot

```
# /etc/rc.local

su pi -c 'python3 /home/pi/django-dms/manage.py runserver 0.0.0.0:8000 &'
```

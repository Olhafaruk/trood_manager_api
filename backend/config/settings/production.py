#settings/production.py

from .base import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600)
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")

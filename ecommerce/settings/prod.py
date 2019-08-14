from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['django-milestone.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

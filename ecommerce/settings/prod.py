from .base import *
import dj_database_url


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['django-milestone.herokuapp.com']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

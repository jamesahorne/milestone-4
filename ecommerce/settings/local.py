from .base import *

SECRET_KEY = 'd1kv7^)qnjxuk%chb$vj$b%*jk21fj2!w6kgdisj26-kq&k#=('

DEBUG = True

ALLOWED_HOSTS = ['9c188c5f89e54468bafff135274c6340.vfs.cloud9.us-east-1.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

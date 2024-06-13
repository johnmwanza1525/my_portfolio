# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hg*$-)srt6=1a6t4+z=scpk%4xgq3nj@apsqxmk*fpej-_2zvz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'portfolio',
            'PASSWORD':'Racer1525$',
            'USER':'john',
            'HOST':'localhost',
            'PORT':'5432',
        }
    }
except DatabaseError:
    pass

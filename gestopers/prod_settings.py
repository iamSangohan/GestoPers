from gestopers.settings import *
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE += [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES['default'] = dj_database_url.config( )

SECRET_KEY = 'nc+v)re0v8s!729@=db08eagk-(knm$-(i&9_0s3zm2(drh0c('

ALLOWED_HOSTS = ['gestopers.herokuapp.com']
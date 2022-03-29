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

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['gestopers.herokuapp.com']
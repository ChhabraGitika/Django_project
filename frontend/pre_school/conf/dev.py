from .common import *
import os

from  dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
    os.path.join(BASE_DIR, "media")
]   

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

"""
Django settings for hotel project.
"""

from pathlib import Path
import os
import mimetypes

# -----------------------------
# BASE DIR
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECURITY SETTINGS
# -----------------------------

# ✅ SECRET_KEY from environment variable, fallback for dev only
SECRET_KEY = os.getenv('SECRET_ENV', 'django-insecure-12345')

# ✅ DEBUG: toggle on/off with environment variable
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ✅ ALLOWED_HOSTS: your domain(s) and local testing
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'myhotel-booking-website.herokuapp.com',
]

# -----------------------------
# APPLICATION DEFINITION
# -----------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Your custom apps
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ for serving static files in prod
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add template dirs if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hotel.wsgi.application'

# -----------------------------
# DATABASE
# -----------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# PASSWORD VALIDATION
# -----------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# -----------------------------
# STATIC FILES
# -----------------------------

STATIC_URL = '/static/'

# ✅ For collectstatic in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ Optional: additional static dirs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "hotels/static"),
]

# ✅ Media files if you have uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/static')

# ✅ Whitenoise fix for serving .css correctly
mimetypes.add_type("text/css", ".css", True)

# -----------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

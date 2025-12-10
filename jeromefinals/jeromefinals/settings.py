"""
Django settings for jeromefinals project.
NO DATABASE - NO ADMIN
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'jeromefinals-secret-key-no-db-required'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jeromefinals.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'jeromefinals.wsgi.application'

# NO DATABASE

# NO PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
#STATIC_URL = 'static/'
#STATICFILES_DIRS = [
#    BASE_DIR / "static"
                    
#]

# Ensure static directory exists
static_dir = BASE_DIR / "static"
if not static_dir.exists():
    os.makedirs(static_dir, exist_ok=True)
    css_dir = static_dir / "css"
    if not css_dir.exists():
        os.makedirs(css_dir, exist_ok=True)

STATICFILES_DIRS = [
    static_dir,
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

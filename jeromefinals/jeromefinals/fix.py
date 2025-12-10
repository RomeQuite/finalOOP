import os

print("Fixing Django project issues...")

# 1. Create static directory if it doesn't exist
static_dir = os.path.join(os.getcwd(), 'static')
css_dir = os.path.join(static_dir, 'css')

if not os.path.exists(static_dir):
    os.makedirs(static_dir)
    print(f"Created: {static_dir}")

if not os.path.exists(css_dir):
    os.makedirs(css_dir)
    print(f"Created: {css_dir}")

# 2. Update settings.py
settings_path = os.path.join(os.getcwd(), 'jeromefinals', 'settings.py')

if os.path.exists(settings_path):
    with open(settings_path, 'r') as f:
        content = f.read()
    
    # Remove any admin or database references
    fixed_content = '''"""
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
STATIC_URL = 'static/'

# Ensure static directory exists
import os
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
'''
    
    with open(settings_path, 'w') as f:
        f.write(fixed_content)
    print("Updated settings.py")
else:
    print(f"Error: {settings_path} not found")

# 3. Update urls.py
urls_path = os.path.join(os.getcwd(), 'jeromefinals', 'urls.py')

with open(urls_path, 'w') as f:
    f.write('''"""
URL configuration for jeromefinals project.
"""

from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
]
''')
print("Updated urls.py")

print("\nFIX COMPLETE!")
print("Now run: python manage.py runserver")
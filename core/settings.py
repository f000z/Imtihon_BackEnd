from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x62)@^gk%o6u#8q-te#dy9gd364pjw9o8n4z^ddv^k^xb-z@=u'

# SECURITY WARNING: don't run with debug turned on in production!
# settings.py

# settings.py
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # или ваш реальный домен


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'shop',
    'drf_yasg',
    'account',
    'locale',
    'widget_tweaks',
]

JAZZMIN_SETTINGS = {
    # General customization
    'site_title': 'Your Admin Site',
    'site_header': 'Your Admin Header',
    'site_brand': 'Fayoz Shop Mebel',
    'site_icon': 'fa fa-cogs',  # Example: Setting a site icon (FontAwesome icon)
    'welcome_sign': 'Welcome to the Admin Panel',

    # Color Scheme Customization
    'theme': 'default',  # Leave 'default' for now (Jazzmin will apply custom colors)
    'color_scheme': {
        # Black background with light green accents
        'background': '#000000',  # Black background
        'header': '#000000',  # Black header background
        'text': '#FFFFFF',  # White text for readability
        'accent': '#90EE90',  # Light green accent color (for buttons, links, etc.)
        'highlight': '#32CD32',  # Another shade of green for highlighting
        'line': '#32CD32',  # Light green line color
    },

    # Sidebar and Nav Customization
    'sidebar': {
        'background_color': '#000000',  # Black background for sidebar
        'text_color': '#FFFFFF',  # White text in sidebar
        'highlight_color': '#32CD32',  # Highlighted color in sidebar
    },

    # Icon Configuration (using FontAwesome icons)
    'icons': {
        'auth': 'fa fa-users',  # Example for 'auth' app
        'shop': 'fa fa-cogs',  # Example for 'shop' app
        'contenttypes': 'fa fa-file',  # Example for 'contenttypes' app
    },

    # Enabling the UI builder (optional)
    'show_ui_builder': False,  # Set to True if you want to enable the UI builder

    # Optional configurations for hiding apps or models
    'hide_apps': [],  # Optionally, specify apps you want to hide
    'hide_models': [],  # Optionally, specify models you want to hide
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'uz-uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
    ('uz', 'O‘zbek tili'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

LOCALE_PATHS = BASE_DIR, 'locale'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

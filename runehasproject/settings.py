"""
Django settings for runehasproject project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^x%pf33=mi@xpbf9p$u#0d!i@_@8+f-b=)hbpwy#a#t=c5i5+!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'runehas',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'runehasproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'runehasproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Authentication backend
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',  # default
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# site ID
SITE_ID = 1

# Setting used by django guardian anonymous users
ANONYMOUS_USER_ID = -1

# cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 'django.core.cache.backends.dummy.DummyCache',
    }
}

# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# settings for static root and collecting static files
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# Uploaded Files ( Images, Text/PDF Files, Videos)
MEDIA_URL = '/media/'

# serving uploaded file in development
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR

# userena URI reflecting
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
USERENA_SIGNIN_AFTER_SIGNUP = True
LOGIN_REDIRECT_URL = '/accounts/signin/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

USERENA_REDIRECT_ON_SIGNOUT = '/'

USERENA_ACTIVATION_REQUIRED = False
USERENA_DISABLE_PROFILE_LIST = True
USERENA_DEFAULT_PRIVACY = 'closed'
# USERENA_PROFILE_DETAIL_TEMPLATE = 'userena/profile_detail.html'

# Userena Settings
USERENA_MUGSHOT_PATH = 'mugshots/'
USERENA_HIDE_EMAIL = True
USERENA_HTML_EMAIL = True

# Auth profile
AUTH_PROFILE_MODULE = 'accounts.MyProfile'

# Gmail email SMTP settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jattoade@gmail.com'
EMAIL_HOST_PASSWORD = 'jasabs93'

# email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# setting for ckeditor upload file path
CKEDITOR_UPLOAD_PATH = "uploads/"
# other ckeditor settings
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_JQUERY_URL = '/static/js/jquery.min.js'  # '/static/vendor/jquery/jquery.min.js'

# ckeditor default config
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full' 'codeSnippets',
        'height': 400,
        'width': 1000,
        'removePlugins': 'stylesheetparser',
        'extraPlugins': 'codesnippet',
    },
}

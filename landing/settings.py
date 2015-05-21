import os
from django.contrib.messages import constants as msg_

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '^x5^z59@kw#umzt4g0j-=60yww#5r2=jr_(&clv%4w30bb5ju9'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'users.User'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.webdesign',
    'compressor',
    'users',
    'core',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.UpdateUserTempMeta',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
)
MESSAGE_TAGS = {
    msg_.DEBUG: '',
    msg_.ERROR: 'uk-alert-danger',
    msg_.WARNING: 'uk-alert-warning',
    msg_.INFO: '',
    msg_.SUCCESS: 'uk-alert-success',
}
ROOT_URLCONF = 'landing.urls'
WSGI_APPLICATION = 'landing.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'landing',
        'USER': 'root',
        'PASSWORD': '405b9c',
        'HOST': '127.0.0.1',
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
STATICFILE_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
MEDIA_URL = '/files/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'
LOGIN_REDIRECT_URL = '/profile/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_AFTER_SIGNUP = True
COMPRESS_ENABLE = True
STATICFILE_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '^x5^z59@kw#umzt4g0j-=60yww#5r2=jr_(&clv%4w30bb5ju9'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'users.User'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'users',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'



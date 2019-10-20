from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '73wy=wy%r^ehl7u)0o+$xy_w@kcmqd!k8@-lmuw8e_uzz0i&e_'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS += [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


INTERNAL_IPS = [
    '127.0.0.1',
]

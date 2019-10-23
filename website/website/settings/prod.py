from .base import *
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


DATABASES['default'] = dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Allow all host headers
ALLOWED_HOSTS = ['*']


sentry_sdk.init(
    dsn=SECRETS['SENTRY_URL'],
    integrations=[DjangoIntegration()]
)

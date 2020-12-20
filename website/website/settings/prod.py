from __future__ import absolute_import, unicode_literals

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

INSTALLED_APPS += [
    "storages",
]

# Media files
AWS_ACCESS_KEY_ID = SECRETS["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = SECRETS["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = SECRETS["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"


# Static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_CSS_HASHING_METHOD = "content"


# Database
DATABASES["default"] = dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


BASE_URL = "https://www.aedug.com"


ALLOWED_HOSTS = ["aedug.com", "www.aedug.com", "quantumrealm.herokuapp.com"]


# Redirect http to https
SECURE_SSL_REDIRECT = True


# Sentry
sentry_sdk.init(
    dsn=SECRETS["SENTRY_URL"],
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)

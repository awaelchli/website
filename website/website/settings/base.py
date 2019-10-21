import json
import os


DEBUG = False


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Secret information like passwords are stored in a json file on the production server.
with open(os.path.join(BASE_DIR, 'secrets.json'), 'r') as file:
    SECRETS = json.load(file)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['SECRET_KEY']


INSTALLED_APPS = [
    'blog',
    'contact',
    'core',
    'flex',
    'home',
    'menus',
    'search',
    'settings',
    'streams',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',
    'wagtail.contrib.sitemaps',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'wagtailfontawesome',
    'captcha',
    'wagtailcaptcha',
    'wagtailcodeblock',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
MEDIA_URL = '/media/'


# Wagtail settings
WAGTAIL_SITE_NAME = "website"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'


# Google reCAPTCHA settings
RECAPTCHA_PUBLIC_KEY = SECRETS['RECAPTCHA']['PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = SECRETS['RECAPTCHA']['PRIVATE_KEY']
NOCAPTCHA = True

# Wagtail code block plugin
WAGTAIL_CODE_BLOCK_THEME = 'default'

WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash + Shell'),
    ('batch', 'Batch'),
    ('c', 'C'),
    ('cpp', 'C++'),
    ('css', 'CSS'),
    ('django', 'Django/Jinja2'),
    ('git', 'Git'),
    ('java', 'Java'),
    ('javascript', 'JavaScript'),
    ('json', 'JSON'),
    ('latex', 'LaTeX'),
    ('makefile', 'Makefile'),
    ('markdown', 'Markdown'),
    ('matlab', 'MATLAB'),
    ('python', 'Python'),
    ('regex', 'Regex'),
    ('sql', 'SQL'),
    ('yaml', 'YAML'),
)
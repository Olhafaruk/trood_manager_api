#backend/config/settings.py

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'projects',
    'vacancy',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Trood Admin",
    "site_header": "TROOD: Admin Panel",
    "site_brand": "Trood",
    "welcome_sign": "Welcome to Trood's internal management",
    "copyright": "© 2025 Trood",
    "topmenu_links": [
        {"name": "Admin Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Documentation", "url": "https://google.com", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "GitHub Issues", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "default_icon_parents": "fas fa-folder-open",
    "default_icon_children": "fas fa-file-alt",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "icons": {
        "auth": "fas fa-users-cog",
        "projects.Project": "fas fa-diagram-project",
        "vacancy.Vacancy": "fas fa-user-tie",
    },
    "order_with_respect_to": ["auth", "projects", "vacancy"],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cyborg",  # или 'darkly', 'lux', 'superhero' — можешь менять
    "sidebar": "sidebar-dark-primary",
    "accent": "accent-teal",
    "navbar": "navbar-dark navbar-primary",
    "brand_colour": "navbar-primary",
    "sidebar_nav_flat_style": True,
    "sidebar_nav_compact_style": True,
}

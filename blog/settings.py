import os
from pathlib import Path

import dj_database_url
import environ

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / ".env"))

# Environment
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS", default=["127.0.0.1", "localhost", ".railway.app"]
)

# Installed apps
INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.import_export",
    "unfold.contrib.filters",
    "unfold.contrib.guardian",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Required for some packages
    # Third-party apps
    "import_export",  # Import/export functionality
    # Your apps
    "posts",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Added for static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # Localization
]

# Root URL configuration
ROOT_URLCONF = "blog.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = "blog.wsgi.application"

DB_PASSWORD = env("DB_PASSWORD")
DATABASE_URL = env("DATABASE_URL")
# Database Configuration

DATABASES = {"default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600)}

# Authentication
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "uz-uz"
TIME_ZONE = env("TIME_ZONE", default="Asia/Tashkent")
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # Location for collected static files
MEDIA_URL = "/assets/"
MEDIA_ROOT = BASE_DIR / "assets"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "error.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

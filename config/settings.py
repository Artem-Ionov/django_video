from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()   # Берём параметры из файла .env
SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "videos.apps.VideosConfig"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # Задаём папки для шаблонов
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Используем PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["NAME"],
        "USER": os.environ["USER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ.get("HOST", "localhost"),    # для docker-compose
        "PORT": "5432"
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Медиафайлы
MEDIA_ROOT = BASE_DIR / "media"  # Папка сохранения для медиафайлов
MEDIA_URL = "/media/"             # URL-префикс

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Перенаправление после входа
LOGIN_REDIRECT_URL = "/videos/"

'''
# Настраиваем логирование
if DEBUG:
    LOGGING = {
        "version": 1,
        # Обработчики логов - определяют куда записывать логи
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG"
            }
        },    
        # Логгеры - определяют что логировать
        "loggers": {
            "django.db.backends": {
                "handlers": ["console"],
                "level": "DEBUG"
            }
        }
    }
    '''

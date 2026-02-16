import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-vgx^wt+bu2)z=qmw8wp#b0l-s(h*$8tf)n=s&&ar(#=d0y%cy_')

# ตรวจสอบว่ารันบน Production หรือไม่
if "DJANGO_DEBUG_FALSE" in os.environ:  
    DEBUG = False
    # ดึงค่าจาก Railway Variables
    db_path = os.environ.get("DJANGO_DB_PATH", "/tmp/db.sqlite3")
    
    # รวม Domain ทั้งหมดไว้ที่เดียวเพื่อป้องกันการเขียนทับ (Overwrite)
    ALLOWED_HOSTS = [
        os.environ.get("DJANGO_ALLOWED_HOST", "*"), # ดึงจาก Variable ถ้าไม่มีให้ใช้ *
        'www.supydev.app', 
        'supydev.app', 
        'goat-production-afa2.up.railway.app', 
        'localhost', 
        '127.0.0.1'
    ]
else:
    DEBUG = True  
    SECRET_KEY = "insecure-key-for-dev"
    ALLOWED_HOSTS = ['*']
    db_path = BASE_DIR / "db.sqlite3"

# แก้ไข CSRF_TRUSTED_ORIGINS (ตัวการที่ทำให้ Error 500)
CSRF_TRUSTED_ORIGINS = [
    'https://www.supydev.app',
    'https://supydev.app',
    'https://goat-production-afa2.up.railway.app'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lists', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # สำหรับเสิร์ฟไฟล์ Static บน Production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        "NAME": db_path,
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging เพื่อดู Error บน Railway
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "loggers": {
        "root": {"handlers": ["console"], "level": "INFO"},
    },
}
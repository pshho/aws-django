"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$v-v3-@t!_+9x=vyz3l_9mm6c+cs^0n^$^_!-h-_*y68#va)y0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    ".ap-northeast-2.compute.amazonaws.com",
    "http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/"
]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = 'true'
# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',  # 로그인 사이트 관련정보를 가져옴(url 관리)
    'allauth',  # 설치한거중 메인기능을 담당한다고함
    'allauth.account',  # 소셜 로그인 회원관리
    'allauth.socialaccount',  # 소셜로그인 정보 관리
    'allauth.socialaccount.providers.google',  # 구글
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'poll',
    'community',
    'notice',
    'information',
    'news',
    'interior',
    'review',
    'introduction',
    'calculate',
    'map',
    'common',
    'koreaCalendar',
    'corsheaders',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    ".ap-northeast-2.compute.amazonaws.com",
    "http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/"
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'
SESSION_COOKIE_AGE = 1800 # 30분 (30 * 60) # 소셜 세션 설정 60초후 초기화
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 소셜 세션 설정 창닫으면 초기화

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = (
    # 로그인 과정 처리 담당
    'django.contrib.auth.backends.ModelBackend',  # 장고에서 제공하는 기본 유저 백엔드
    'allauth.account.auth_backends.AuthenticationBackend',  # 소셜로그인 allauth가 제공하는 정보가 있음
)

LOGIN_REDIRECT_URL = '/'  # 로그인하고 갈 페이지 설정
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'ALLOWALL' # iframe 제거 테스트


LOGOUT_REDIRECT_URL = '/' #로그아웃 성공시 루트로 이동


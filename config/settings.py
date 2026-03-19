import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY='x'
DEBUG=True
ALLOWED_HOSTS=['*']

INSTALLED_APPS=[
'django.contrib.contenttypes',
'django.contrib.staticfiles',
'supervision',
]

MIDDLEWARE=[]

ROOT_URLCONF='config.urls'

TEMPLATES=[{
'BACKEND':'django.template.backends.django.DjangoTemplates',
'DIRS':[BASE_DIR/'supervision/templates'],
'APP_DIRS':True,
}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}

STATIC_URL='/static/'

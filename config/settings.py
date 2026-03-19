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

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

print("USANDO DB:", os.environ["DB_HOST"])

STATIC_URL='/static/'

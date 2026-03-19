from django.urls import path
from .views import dashboard, exportar_csv

urlpatterns=[
path('',dashboard),
path('exportar/',exportar_csv),
]

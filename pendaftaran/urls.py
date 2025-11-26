from django.urls import path
from .views import index, register, check_status

app_name = 'pendaftaran'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('check-status/', check_status, name='check_status'),
]

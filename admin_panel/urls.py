from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('manage/', views.manage, name='manage'),
    path('verify/<int:pk>/', views.verify, name='verify'),
    path('delete/<int:pk>/', views.delete_wartawan, name='delete_wartawan'),
    path('report/', views.report, name='report'),
    path('logout/', views.logout_view, name='logout'),
    path('auto-verify/', views.auto_verify, name='auto_verify'),
]

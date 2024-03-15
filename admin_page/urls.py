from django.urls import path
from admin_page import views

urlpatterns = [
    path('', views.admin_page, name='admin_page')
]
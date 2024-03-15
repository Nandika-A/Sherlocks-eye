from django.urls import path
from main import views

urlpatterns = [
    path('', views.test_emotions, name='test_emotions'),
]
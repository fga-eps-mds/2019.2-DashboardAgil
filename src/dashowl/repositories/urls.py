from django.urls import path
from . import views

urlpatterns = [
    path('', views.repositories, name='repositories'),
]
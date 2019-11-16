from django.urls import path

from . import  views

urlpatterns = [
    path('', views.commits, name='commits')

]
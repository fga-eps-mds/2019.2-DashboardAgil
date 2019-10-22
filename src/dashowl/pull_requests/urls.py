from django.urls import path
from . import views

urlpatterns = [
    path('', views.openPullRuequests, name='pull_requests'),
]
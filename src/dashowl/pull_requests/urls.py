from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_PullRuequests, name='pull_requests'),
]
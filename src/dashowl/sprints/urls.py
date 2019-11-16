from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sprints, name='sprints'),
]
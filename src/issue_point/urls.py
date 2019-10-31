from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_issue_points,name='issue_point')
]

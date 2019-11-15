from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.get_commits, name='commits'),
=======
from . import  views

urlpatterns = [
    path('', views.commits, name='commits')
>>>>>>> devel
]
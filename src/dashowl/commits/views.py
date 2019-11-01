from django.shortcuts import render
from github import Github

# Create your views here.


def commits(request):
    g = Github("")
    teste = "deu certo"
    return render(request, 'commits.html', {'commit':teste})
    
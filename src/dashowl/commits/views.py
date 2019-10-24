from django.shortcuts import render

# Create your views here.
def commits(request):
    teste = "deu certo"
    return render(request, 'commits.html', {'commit':teste})
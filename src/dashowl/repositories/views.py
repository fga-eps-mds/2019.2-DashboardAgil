from django.shortcuts import render


def repositories(request):
    return render(request, 'repositories.html', {})
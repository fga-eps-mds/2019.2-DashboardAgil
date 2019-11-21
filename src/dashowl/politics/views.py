from django.shortcuts import render


def politics(request):
    return render(request, 'politics.html', {})
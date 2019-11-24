from django.shortcuts import render


def invite(request):
    return render(request, 'invite.html', {})
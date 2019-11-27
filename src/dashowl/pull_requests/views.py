from django.shortcuts import render
from github import Github
from .models import Pull_request
from .. import secret
import datetime


def get_PullRuequests (request):
    # token = Usuario.token
    # g = Github(token)
    # repos = Usuario.repos
    # repo = g.get_repo(repos[])
    
    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")

    if bool(Pull_request.objects.filter(repository__repositoryID=repo.id)):
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id)
        #pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
        #pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')

        date1o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=1)
        date2o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=2)
        date3o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=3)
        date4o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=4)
        date5o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=5)
        date6o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=6)
        date7o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=7)
        date8o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=8)
        date9o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=9)
        date10o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=10)
        date11o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=11)
        date12o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=12)

        date1c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=1, state='closed')
        date2c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=2, state='closed')
        date3c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=3, state='closed')
        date4c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=4, state='closed')
        date5c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=5, state='closed')
        date6c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=6, state='closed')
        date7c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=7, state='closed')
        date8c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=8, state='closed')
        date9c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=9, state='closed')
        date10c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=10, state='closed')
        date11c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=11, state='closed')
        date12c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=12, state='closed')


    else:
        raise TypeError

    
    return render(request, 'pull_requests.html', {'pull_requests': pull_requests, 'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o,'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})


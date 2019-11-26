from django.shortcuts import render
from github import Github
from .models import Pull_request
from .. import secret


def get_PullRuequests (request):
    # token = Usuario.token
    # g = Github(token)
    # repos = Usuario.repos
    # repo = g.get_repo(repos[])
    
    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")


    if bool(Pull_request.objects.filter(repository__repositoryID=repo.id)):
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id)
        pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
        pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')
    else:
        raise TypeError


    return render(request, 'pull_requests.html', {'pull_requests': pull_requests, 'pulls_open': pulls_open, 'pulls_closed': pulls_closed})


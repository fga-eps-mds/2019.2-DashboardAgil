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
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
        pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
        pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')
        refresh_pull_requests(repo, list(pull_requests)[-1].repository, list(pull_requests)[-1].pull_request_number)

    else:
        raise TypeError

    return render(request, 'pull_requests.html', {'pull_requests': pull_requests, 'pulls_open': pulls_open, 'pulls_closed': pulls_closed})


def refresh_pull_requests(repo, repository, last):
    pull_requests = repo.get_pulls(state='all')
    for i in range(last+1, pull_requests.totalCount):
        pull_requests_model = Pull_request.objects.create(repository=repository,
                                                          pull_request_number=pull_requests[i].number,
                                                          state=pull_requests[i].state,
                                                          author=pull_requests[i].user.login,
                                                          open_date=pull_requests[i].created_at)
        pull_requests_model.publish()

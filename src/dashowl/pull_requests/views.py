from django.shortcuts import render
from github import Github
from .models import Pull_request
from .. import secret
from ..repositories.views import REPO_ATUAL
from ..repositories.models import Repository


def get_PullRuequests (request):
    user_login = request.session['login']
    token = request.session['token']

    # g = Github(login_or_token=token)
    g = Github(login_or_token=user_login, password=secret.password)
    repo = g.get_repo(full_name_or_id=REPO_ATUAL)

    repository = Repository.objects.get(repositoryID=repo.id)
    if bool(Pull_request.objects.filter(repository__repositoryID=repo.id)):
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
        refresh_pull_requests(repo, list(pull_requests)[-1].repository, list(pull_requests)[-1].pull_request_number)
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
        pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
        pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')

    else:
        save_pull_request(repo, repository)
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
        pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
        pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')


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


def save_pull_request(repo, repository):
    pull_requests = repo.get_pulls(state='all')
    if bool(list(pull_requests)):
        for pull_request in pull_requests:
            pull_requests_model = Pull_request.objects.create(repository=repository,
                                                              pull_request_number=pull_request.number,
                                                              state=pull_request.state,
                                                              author=pull_request.user.login,
                                                              open_date=pull_request.created_at)
            pull_requests_model.publish()
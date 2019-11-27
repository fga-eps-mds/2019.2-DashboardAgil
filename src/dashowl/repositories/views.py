from django.shortcuts import render
from github import Github
from .models import Repository
#from .. import secret
from ..index.models import Usuario
from ..commits.models import Commit
from ..milestone.models import Milestone
from ..issues.models import Issue
from ..pull_requests.models import Pull_request


REPO_ATUAL = "fga-eps-mds/2019.2-DashboardAgil"

def repositories(request):

    user_login = request.session['login']
    token = request.session['token']
    g = Github(token)
    repos_names = []
    repos_id = []
    if bool(Repository.objects.filter(user__login=user_login)):
        user = Usuario.objects.get(login=user_login)
        repos = Repository.objects.filter(user__login=user_login)
        refresh_repos(g, user, list(repos)[-1].id)
        repos = Repository.objects.filter(user__login=user_login)
        for repository in repos:
            repos_names.append(repository.name)
            repos_id.append(repository.id)
    else:
        user = Usuario.objects.get(login=user_login)
        for repository in g.get_user().get_repos(type='owner'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)
            repos_id.append(repository.id)
        
        for repository in g.get_user().get_repos(type='member'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)
            repos_id.append(repository.id)
  
        for repository in g.get_user().get_repos(type='private'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)
            repos_id.append(repository.id)

    repos = zip(repos_names, repos_id)

    return render(request, 'repositories.html', {'repos': repos})


def refresh_repos(g, user, last):
    repos = g.get_user().get_repos(type='member')
    for i in range(last+1, repos.totalCount):
        repository_model = Repository.objects.create(user=user,
                                                     name=repos[i].name,
                                                     repositoryID=repos[i].id)
        repository_model.publish()

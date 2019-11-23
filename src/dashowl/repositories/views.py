from django.shortcuts import render
from github import Github
from .models import Repository
from .. import secret
from ..index.models import Usuario

def repositories(request):

    user_login = secret.login
    password = secret.password
    g = Github(login_or_token=user_login, password=password)
    repos_names = []
    if bool(Repository.objects.filter(user__login=user_login)):
        repos = Repository.objects.filter(user__login=user_login)
        for repository in repos:
            repos_names.append(repository.name)
    else:
        for repository in g.get_user().get_repos(type='member'):
            user = Usuario.objects.get(login=user_login)
            repository_model = Repository.objects.create(user=user, name=repository.name, repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)

    return render(request, 'repositories.html', {'repos': repos_names})
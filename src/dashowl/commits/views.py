from django.shortcuts import render
from github import Github
from .models import Commit
from .. import secret
from ..repositories.models import Repository


def get_commits(request):

    g = Github(login_or_token=secret.login, password=secret.password)
    repo = g.get_repo(full_name_or_id="fga-eps-mds/2019.2-DashboardAgil")
    """
    Falta se livrar dessa parte aqui e só pegar o id que o usuário escolher
    """

    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id)
    else:
        raise TypeError

    return render(request, 'commits.html', {'commits': commits})

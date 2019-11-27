from datetime import datetime
from django.shortcuts import render
from github import Github
from .models import Commit
from .. import secret
from ..repositories.views import REPO_ATUAL

def get_commits(request):

    # g = Github(login_or_token=TOKEN)
    g = Github(login_or_token=secret.login, password=secret.password)

    repo = g.get_repo(full_name_or_id=REPO_ATUAL)
    """
    Falta se livrar dessa parte aqui e só pegar o id que o usuário escolher
    """

    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')
        refresh_commits(repo, list(commits)[-1].repository, list(commits)[-1].date)
    else:
        raise TypeError

    return render(request, 'commits.html', {'commits': commits})


def refresh_commits(repo, repository, last):
    for commit in repo.get_commits(since=last):
        commit_model = Commit.objects.create(repository=repository,
                                             sha_commit=commit.sha,
                                             author=commit.commit.author.name,
                                             date=commit.commit.author.date)
        commit_model.publish()
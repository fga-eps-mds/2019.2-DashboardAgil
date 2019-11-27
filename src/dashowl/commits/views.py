from datetime import datetime
from django.shortcuts import render
from github import Github
from .models import Commit
from .. import secret
from ..repositories.views import REPO_ATUAL
from ..repositories.models import Repository

def get_commits(request):

    user_login = request.session['login']
    token = request.session['token']

    # g = Github(login_or_token=token)
    g = Github(login_or_token=user_login, password=secret.password)
    repo = g.get_repo(full_name_or_id=REPO_ATUAL)

    """
    Falta se livrar dessa parte aqui e só pegar o id que o usuário escolher
    """

    repository = Repository.objects.get(repositoryID=repo.id)
    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')
        refresh_commits(repo, repository, list(commits)[-1].date)
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')
    else:
        save_commit(repo, repository)
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')

    return render(request, 'commits.html', {'commits': commits})


def refresh_commits(repo, repository, last):
    for commit in repo.get_commits(since=last):
        commit_model = Commit.objects.create(repository=repository,
                                             sha_commit=commit.sha,
                                             author=commit.commit.author.name,
                                             date=commit.commit.author.date)
        commit_model.publish()


def save_commit(repo, repository):
    commits = repo.get_commits()
    if bool(list(commits)):
        for commit in commits:
            commit_model = Commit.objects.create(repository=repository,
                                                 sha_commit=commit.sha,
                                                 author=commit.commit.author.name,
                                                 date=commit.commit.author.date)
            commit_model.publish()
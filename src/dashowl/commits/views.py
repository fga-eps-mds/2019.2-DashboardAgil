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

<<<<<<< HEAD
    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    commits = repo.get_commits()
    totalCommits = commits.totalCount

    # for commit in repo.get_commits():
    #     commit_model = Commit.objects.create(shaCommit=commit.sha, author=commit.commit.author.name, date=commit.commit.author.date)
    #     commit_model.publish()

    # print(commit.commit.author.date)
=======
    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id)
        # refresh_commit(commits[0].repository)
    else:
        raise TypeError
>>>>>>> c6bc0e2dfadccf4b2edd97efcdb7d7a15dc9be90

    return render(request, 'commits.html', {'commits': commits})


def refresh_commit(repository):
    Commit.objects.all().exclude(repository=repository)
    g = Github(login_or_token=secret.login, password=secret.password)
    repo = g.get_repo(full_name_or_id=repository.repositoryID)
    for commit in repo.get_commits():
        commit_model = Commit.objects.create(repository=repository,
                                             sha_commit=commit.sha,
                                             author=commit.commit.author.name,
                                             date=commit.commit.author.date)
        commit_model.publish()

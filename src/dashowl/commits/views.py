from django.shortcuts import render
from github import Github
from .models import Commit
from .. import secret
from ..repositories.models import Repository


def get_commits(request):

    g = Github(login_or_token=secret.login, password=secret.password)

    repository_full_name = "fga-eps-mds/2019.2-DashboardAgil"
    repo = g.get_repo(full_name_or_id=repository_full_name)

    commit_authors = []
    commit_sha = []
    commit_date = []
    commit_total = int(0)
    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):
        commits = Commit.objects.filter(repository__repositoryID=repo.id)
        for commit in commits:
            commit_authors.append(commit.author)
            commit_sha.append(commit.sha_commit)
            commit_date.append(commit.date)
            commit_total += 1
    else:
        raise TypeError


    commits = repo.get_commits()
    total_commits = commits.totalCount
    return render(request, 'commits.html', {'commit':commits, 'total':commit_total})

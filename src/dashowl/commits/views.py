from django.shortcuts import render
from github import Github

# from .models import Usuario

# Create your views here.


def commits(request):

    # token = Usuario.token
    # g = Github(token)
    # repos = Usuario.repos
    # repo = g.get_repo(repos[])
    # repo.get_commit(sha)
    # repo.get_commits(sha=NotSet, path=NotSet, since=NotSet, until=NotSet, author=NotSet)

    g = Github("joao15victor08", "j15v08o19m99")
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    commits = repo.get_commits()
    totalCommits = commits.totalCount
    # commit = repo.get_commit(sha="7c8c4aba33040cf9865a40703900ca797bc816b4")
    # print(commit.commit.author.date)


    return render(request, 'commits.html', {'commit':commits, 'total':totalCommits})
    

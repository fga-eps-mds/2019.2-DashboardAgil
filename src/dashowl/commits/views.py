from django.shortcuts import render
from github import Github
from .models import Commit
# from .models import Usuario


def get_commits(request):

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

    for commit in repo.get_commits():
        commit_model = Commit.objects.create(shaCommit=commit.sha, author=commit.commit.author.name, date=commit.commit.author.date)
        commit_model.publish()

    # print(commit.commit.author.date)



    return render(request, 'commits.html', {'commit':commits, 'total':totalCommits})
    
# def saveCommits(request):
#     commit_form = CommitForm(request.POST)
#     if commit_form.is_valid():
#         commit_form.save()

#     context = {
#         'commit_form' : commit_form
#     }
#     return render(request, 'save_commits.html', context=context)
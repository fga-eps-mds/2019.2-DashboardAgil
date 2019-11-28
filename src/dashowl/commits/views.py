from django.shortcuts import render
from github import Github
from .models import Commit
#from .. import secret
from ..repositories.models import Repository


def get_commits(request):

    token = request.session['token']    

    repo_id = request.GET["id"]

    request.session['id'] = repo_id

    g = Github(token)
    repo = g.get_repo(int(repo_id))
    commits = repo.get_commits()
    total_commits = commits.totalCount
    autoresc = Commit.objects.filter(repository__repositoryID=repo.id).order_by('author').distinct('author')
    repository = Repository.objects.get(repositoryID=repo.id)

    if bool(Commit.objects.filter(repository__repositoryID=repo.id)):

        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')
        refresh_commits(repo, repository, list(commits)[-1].date)
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')

        commits = Commit.objects.filter(repository__repositoryID=repo.id)
        author1 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'Matheus-AM')
        author1 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'Matheus-AM')
        author2 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'KalebeLopes')
        author3 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'joao15victor08')
        author4 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'ailamaralves')
        author5 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'muriloschiler')
        author6 = Commit.objects.filter(repository__repositoryID=repo.id, author = 'damarcones')

        date1o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=1)
        date2o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=2)
        date3o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12o = Commit.objects.filter(repository__repositoryID=repo.id, date__month=12)

        date1c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=1 )
        date2c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=2 )
        date3c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12c = Commit.objects.filter(repository__repositoryID=repo.id, date__month=12)

    else:
        save_commit(repo, repository)
        commits = Commit.objects.filter(repository__repositoryID=repo.id).order_by('date')

    return render(request, 'commits.html', {'commits': commits, 'autoresc': autoresc,'total_commits': total_commits, 
     'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o, 'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})






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
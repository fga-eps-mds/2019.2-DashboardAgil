from django.shortcuts import render
from github import Github
import requests
import json
from .models import Issue
#from .. import secret
from ..repositories.models import Repository


#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc


def get_issues(request):

    token = request.session['token']
    repo_id = request.session['id']


    g = Github(token)
    repo = g.get_repo(int(repo_id))    

    repository = Repository.objects.get(repositoryID=repo.id)

    if bool(Issue.objects.filter(repository__repositoryID=repo.id)):
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id).order_by('date')
        refresh_issues(repo, repository, list(all_issues)[-1].date)

        date1o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1)
        date2o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2)
        date3o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12)

        date1c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1, state='closed')
        date2c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2, state='closed')
        date3c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3, state='closed')
        date4c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4, state='closed')
        date5c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5, state='closed')
        date6c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6, state='closed')
        date7c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7, state='closed')
        date8c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8, state='closed')
        date9c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9, state='closed')
        date10c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10, state='closed')
        date11c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11, state='closed')
        date12c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12, state='closed')


    else:
        save_issue(repo, repository)
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id)

        date1o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1)
        date2o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2)
        date3o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12)

        date1c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1, state='closed')
        date2c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2, state='closed')
        date3c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3, state='closed')
        date4c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4, state='closed')
        date5c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5, state='closed')
        date6c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6, state='closed')
        date7c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7, state='closed')
        date8c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8, state='closed')
        date9c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9, state='closed')
        date10c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10, state='closed')
        date11c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11, state='closed')
        date12c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12, state='closed')


#Retorna o valor de cada issue
    # req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    # issue_json = req.json()
    # point_issue = issue_json["estimate"]["value"]


    return render(request, 'issues.html', { 'all_issues': all_issues,
     'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o, 'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})

def refresh_issues(repo, repository, last):
    for issue in repo.get_issues(state='all', since=last):
        issues_model = Issue.objects.create(repository=repository,
                                            issue_number=issue.number,
                                            state=issue.state,
                                            author=issue.user.login,
                                            date=issue.created_at)
        issues_model.publish()


def save_issue(repo, repository):
    issues = repo.get_issues(state='all')
    if bool(list(issues)):
        for issue in issues:
            issues_model = Issue.objects.create(repository=repository,
                                                issue_number=issue.number,
                                                state=issue.state,
                                                author=issue.user.login,
                                                date=issue.created_at)
            issues_model.publish()
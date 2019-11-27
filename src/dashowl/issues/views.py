from django.shortcuts import render
from github import Github
import requests
import json
from .models import Issue
from .. import secret


#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc


def get_issues(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
    """
        dar um jeito de pegar o id do repositório atual
    """

    if bool(Issue.objects.filter(repository__repositoryID=repo.id)):
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id).order_by('date')
        open_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='open')
        closed_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='closed')
        refresh_issues(repo, list(all_issues)[-1].repository, list(all_issues)[-1].date)
    else:
        raise TypeError

#Retorna o valor de cada issue
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]


    return render(request, 'issues.html', {'aissues': aissues, 'all_issues': all_issues, 'all_issues': all_issues, 
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
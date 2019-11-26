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
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id)
        open_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='open')
        closed_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='closed')

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


    else:
        raise TypeError

#Retorna o valor de cada issue
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]

    return render(request, 'issues.html', {'open_issues': open_issues, 'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o})



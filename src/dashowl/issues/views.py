from django.shortcuts import render
from github import Github
import requests
import json
from .models import Issues


#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc


def get_issues(request):

    g = Github("joao15victor08", "j15v08o19m99")
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
    #   ISSUES ABERTAS 
    open_issues = repo.get_issues(state='open')

#   ISSUES FECHADAS
    closed_issues = repo.get_issues(state='closed')

#   TODAS AS ISSUES 
    all_issues = repo.get_issues(state='all')

#   ISSUES CREATOR 
    creator_issues = repo.get_issues(creator='Matheus-AM')#precisasmos de uma variavel de usuario

    for issue in repo.get_issues(state='all'):
        issues_model = Issues.objects.create(issue_number=issue.number, state=issue.state, date=issue.created_at)
        issues_model.publish()


#Retorna o valor de cada issue 
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')     
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]
    
    return render(request, 'issues.html', {'open_issues': open_issues,'closed_issues': closed_issues,'all_issues': all_issues,'creator_issues': creator_issues, 'point_issues': point_issue})



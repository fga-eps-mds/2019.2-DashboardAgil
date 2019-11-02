from django.shortcuts import render
from github import Github
import requests
import json
#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc

def get_issues(request):

    g = Github("KalebeLopes", "")#pode ser o acess_token do github
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
    #   ISSUES ABERTAS 
    open_issues = repo.get_issues(state='open')

#   ISSUES FECHADAS
    closed_issues = repo.get_issues(state='closed')

#   TODAS AS ISSUES 
    all_issues = repo.get_issues(state='all')

#   ISSUES CREATOR 
    creator_issues = repo.get_issues(creator='Matheus-AM')#precisasmos de uma variavel de usuario

#Retorna o valor de cada issue 
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=88ecf0f6ad902fa218d3eb2be63b0ff1a4b2f53b3c49aa9493279638612cf7657d22dc87e6892bc3')     
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]
    
    return render(request, 'issues.html', {'open_issues': open_issues,'closed_issues': closed_issues,'all_issues': all_issues,'creator_issues': creator_issues,'point_issues':point_issue})



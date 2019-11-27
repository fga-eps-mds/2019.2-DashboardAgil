from django.shortcuts import render
from github import Github
import requests
import json
from .models import Issue
from .. import secret
from ..repositories.views import REPO_ATUAL
from ..repositories.models import Repository


#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc


def get_issues(request):

    user_login = request.session['login']
    token = request.session['token']

    # g = Github(login_or_token=token)
    g = Github(login_or_token=user_login, password=secret.password)
    repo = g.get_repo(full_name_or_id=REPO_ATUAL)

    """
        dar um jeito de pegar o id do repositório atual
    """
    repository = Repository.objects.get(repositoryID=repo.id)
    if bool(Issue.objects.filter(repository__repositoryID=repo.id)):
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id).order_by('date')
        refresh_issues(repo, repository, list(all_issues)[-1].date)
        open_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='open')
        closed_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='closed')
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id)
    else:
        save_issue(repo, repository)
        open_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='open')
        closed_issues = Issue.objects.filter(repository__repositoryID=repo.id, state='closed')
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id)

#Retorna o valor de cada issue
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]

    return render(request, 'issues.html', {'open_issues': open_issues, 'closed_issues': closed_issues, 'all_issues': all_issues, 'point_issues': point_issue})


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

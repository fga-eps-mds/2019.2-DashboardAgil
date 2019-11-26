from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret


def get_milestone(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')

    if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
        milestones = Milestone.objects.filter(repository__repositoryID=repo.id)
        milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
        milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')
    else:
        raise TypeError


    return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})

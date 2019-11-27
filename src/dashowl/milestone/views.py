from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret


def get_milestone(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')
    open_milestone = repo.get_milestones(state='all')

    if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
        milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
        milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
        milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')
        refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestone_number)

    else:
        raise TypeError

    return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})


def refresh_milestones(repo, repository, last):
    milestones = repo.get_milestones(state='all')
    for i in range(last+1, milestones.totalCount):
        milestone_model = Milestone.objects.create(repository=repository,
                                                   milestone_number=milestones[i].number,
                                                   state=milestones[i].state,
                                                   title=milestones[i].title,
                                                   author=milestones[i].creator.login,
                                                   created_at=milestones[i].created_at,
                                                   due_on=milestones[i].due_on)
        milestone_model.publish()
#Retorna o valor de cada issue
    # req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    # issue_json = req.json()
    # point_issue = issue_json["estimate"]["value"]?code=eb1a6036e5788eb01425
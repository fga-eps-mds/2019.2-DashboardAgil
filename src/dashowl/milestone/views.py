from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret


def get_milestone(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')

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

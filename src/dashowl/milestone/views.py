from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret


def get_milestone(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')
    open_milestone = repo.get_milestones(state='all')

    # salvar no banco
    for milestone in repo.get_milestones(state='all'):
        milestone_model = Milestone.objects.create(milestoneID=milestone.id,
                                                   state=milestone.state,
                                                   title=milestone.title,
                                                   author=milestone.creator.login,
                                                   created_at=milestone.created_at,
                                                   due_on=milestone.due_on)
        milestone_model.publish()

    # salvar no banco

    return render(request, 'milestone.html', {'milestone': open_milestone})

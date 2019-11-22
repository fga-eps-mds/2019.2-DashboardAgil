from django.shortcuts import render
from github import Github
from .models import Milestones


def get_milestone(request):

    g = Github('joao15victor08', 'j15v08o19m99')
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')
    open_milestone = repo.get_milestones(state='open')

    # salvar no banco
    for milestone in repo.get_milestones(state='open'):
        milestone_model = Milestones.objects.create(milestoneID=milestone.id, state=milestone.state, title=milestone.title, due_on=milestone.due_on)
        milestone_model.publish()
    for milestone in repo.get_milestones(state='close'):
        milestone_model = Milestones.objects.create(milestoneID=milestone.id, state=milestone.state, title=milestone.title, due_on=milestone.due_on)
        milestone_model.publish()
    # salvar no banco

    return render(request, 'milestone.html', {'milestone': open_milestone})

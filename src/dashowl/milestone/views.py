from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret
from ..repositories.models import Repository


def get_milestone(request):

    repo_id = request.GET["id"]

    token = request.session['token']


    g = Github(token)

    r = Repository.objects.get(repositoryID=repo_id)

    repo = g.get_repo(r.name)


    if bool(Milestone.objects.filter(repository__repositoryID=repo_id)):
        milestones = Milestone.objects.filter(repository__repositoryID=repo_id)
        milestones_open = Milestone.objects.filter(repository__repositoryID=repo_id, state='open')
        milestones_closed = Milestone.objects.filter(repository__repositoryID=repo_id, state='closed')
    else:
        for milestone in repo.get_milestones(state='all'):
            milestone_model = Milestone.objects.create(repository=repo,
                                                   milestoneID=milestone.id,
                                                   state=milestone.state,
                                                   title=milestone.title,
                                                   author=milestone.creator.login,
                                                   created_at=milestone.created_at,
                                                   due_on=milestone.due_on)
    

    return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})

from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret
from ..repositories.views import REPO_ATUAL
from ..repositories.models import Repository


def get_milestone(request):
    user_login = request.session['login']
    token = request.session['token']

    # g = Github(login_or_token=token)
    g = Github(login_or_token=user_login, password=secret.password)
    repo = g.get_repo(full_name_or_id=REPO_ATUAL)

    repository = Repository.objects.get(repositoryID=repo.id)
    if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
        milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
        refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestone_number)
        milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
        milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
        milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

    else:
        save_milestone(repo, repository)
        milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
        milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
        milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

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


def save_milestone(repo, repository):
    for milestone in repo.get_milestones(state='all'):
        milestone_model = Milestone.objects.create(repository=repository,
                                                   milestone_number=milestone.number,
                                                   state=milestone.state,
                                                   title=milestone.title,
                                                   author=milestone.creator.login,
                                                   created_at=milestone.created_at,
                                                   due_on=milestone.due_on)
        milestone_model.publish()

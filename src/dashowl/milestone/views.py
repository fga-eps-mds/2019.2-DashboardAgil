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
        if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
            all_milestone = Milestone.objects.filter(repository__repositoryID=repo.id)
            open_milestone = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
            closed_milestone = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')
        else:
            raise TypeError

#Retorna o valor de cada issue
    # req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    # issue_json = req.json()
    # point_issue = issue_json["estimate"]["value"]

    return render(request, 'milestone.html', {'open_milestone': open_milestone, 'closed_milestone': closed_milestone})

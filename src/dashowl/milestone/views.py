from django.shortcuts import render
from github import Github

def milestone(request):

    g = Github('joao15victor08', 'j15v08o19m99')
    repo = g.get_repo('fga-eps-mds/2019.2-DashboardAgil-Wiki')
    open_milestone = repo.get_milestones(state = 'open')

    return render(request, 'milestone.html', {'milestone':open_milestone})

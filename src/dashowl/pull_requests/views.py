from django.shortcuts import render
from github import Github

# from .models import Usuario

# Create your views here.

def get_PullRuequests (request):
    # token = Usuario.token
    # g = Github(token)
    # repos = Usuario.repos
    # repo = g.get_repo(repos[])
    
    g = Github("joao15victor08", "j15v08o19m99")
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    pulls_open = repo.get_pulls(state = "open")
    pulls_closed = repo.get_pulls(state = "closed")
    total = pulls_open.totalCount
    total+=pulls_closed.totalCount

    return render(request, 'pull_requests.html', {'pulls_open': pulls_open,'pulls_closed':pulls_closed,'total': total})
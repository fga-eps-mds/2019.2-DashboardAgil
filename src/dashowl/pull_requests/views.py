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
    total_open = pulls_open.totalCount

    pulls_closed = repo.get_pulls(state = "closed")
    total_closed = pulls_closed.totalCount

    total = total_open + total_closed

    #comments = repo.comments.value(state = "comments")

    return render(request, 'pull_requests.html', {'pulls_open': pulls_open, 'total_open': total_open, 'pulls_closed':pulls_closed,'total': total})
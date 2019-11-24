from django.shortcuts import render
from github import Github
from .models import Pull_request
from .. import secret

# from .models import Usuario

# Create your views here.

def get_PullRuequests (request):
    # token = Usuario.token
    # g = Github(token)
    # repos = Usuario.repos
    # repo = g.get_repo(repos[])
    
    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    pulls_open = repo.get_pulls(state="open")
    pulls_closed = repo.get_pulls(state="closed")
    total = pulls_open.totalCount
    total += pulls_closed.totalCount

    # salvar no banco
    for pull_request in repo.get_pulls(state='all'):
        pull_requests_model = Pull_request.objects.create(pull_request_number=pull_request.number,
                                                          state=pull_request.state,
                                                          author=pull_request.user.login,
                                                          open_date=pull_request.created_at)
        pull_requests_model.publish()
    # salvar no banco

    return render(request, 'pull_requests.html', {'pulls_open': pulls_open, 'pulls_closed': pulls_closed, 'total': total})
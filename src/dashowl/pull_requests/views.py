from django.shortcuts import render
from github import Github
from .models import Pull_request
#from .. import secret
from ..repositories.models import Repository
import datetime


def get_PullRuequests (request):
    
    token = request.session['token']
    repo_id = request.session['id']
    
    g = Github(token)
    repo = g.get_repo(int(repo_id))
    autorespr = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('author').distinct('author')

    repository = Repository.objects.get(repositoryID=repo.id)

    if bool(Pull_request.objects.filter(repository__repositoryID=repo.id)):
        pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
        refresh_pull_requests(repo, list(pull_requests)[-1].repository, list(pull_requests)[-1].pull_request_number)
    else:
        save_pull_request(repo, repository)

    pull_requests = Pull_request.objects.filter(repository__repositoryID=repo.id).order_by('pull_request_number')
    #pulls_open = Pull_request.objects.filter(repository__repositoryID=repo.id, state='open')
    #pulls_closed = Pull_request.objects.filter(repository__repositoryID=repo.id, state='closed')

    date1o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=1)
    date2o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=2)
    date3o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=3)
    date4o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=4)
    date5o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=5)
    date6o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=6)
    date7o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=7)
    date8o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=8)
    date9o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=9)
    date10o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=10)
    date11o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=11)
    date12o = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=12)

    date1c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=1, state='closed')
    date2c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=2, state='closed')
    date3c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=3, state='closed')
    date4c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=4, state='closed')
    date5c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=5, state='closed')
    date6c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=6, state='closed')
    date7c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=7, state='closed')
    date8c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=8, state='closed')
    date9c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=9, state='closed')
    date10c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=10, state='closed')
    date11c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=11, state='closed')
    date12c = Pull_request.objects.filter(repository__repositoryID=repo.id, open_date__month=12, state='closed')


    return render(request, 'pull_requests.html', {'autorespr': autorespr, 'pull_requests': pull_requests, 'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
     'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o,'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})


def save_pull_request(repo, repository):
    pull_requests = repo.get_pulls(state='all')
    if bool(list(pull_requests)):
        for pull_request in pull_requests:
            pull_requests_model = Pull_request.objects.create(repository=repository,
                                                              pull_request_number=pull_request.number,
                                                              state=pull_request.state,
                                                              author=pull_request.user.login,
                                                              open_date=pull_request.created_at)
            pull_requests_model.publish()


def refresh_pull_requests(repo, repository, last):
    pull_requests = repo.get_pulls(state='all')
    for i in range(last+1, pull_requests.totalCount):
        pull_requests_model = Pull_request.objects.create(repository=repository,
                                                          pull_request_number=pull_requests[i].number,
                                                          state=pull_requests[i].state,
                                                          author=pull_requests[i].user.login,
                                                          open_date=pull_requests[i].created_at)
        pull_requests_model.publish()
from django.shortcuts import render
from github import Github
from .models import Milestone
#from .. import secret
from ..repositories.models import Repository


def get_milestone(request):
    
    if 'id' not in request.session:
        if request.method == 'GET' and 'id' in request.GET:

            user_login = request.session['login']
            token = request.session['token']

            repo_id = request.session['id']

            g = Github(token)
            
            repo = g.get_repo(full_name_or_id=int(repo_id))

            repository = Repository.objects.get(repositoryID=repo.id)
            if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestoneID)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            else:
                save_milestone(repo, repository)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})
        else:
            sem_id = "Selecione um repositório"
            return render(request, 'milestone.html', {'id':sem_id})
    else:
        if request.method == 'GET' and 'id' in request.GET:
            user_login = request.session['login']
            token = request.session['token']

            repo_id = request.GET["id"]

            request.session['id'] = repo_id

            g = Github(token)
            
            repo = g.get_repo(full_name_or_id=int(repo_id))

            repository = Repository.objects.filter(repositoryID=repo.id)
            if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestoneID)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            else:
                save_milestone(repo, repository)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})
        else:
            user_login = request.session['login']
            token = request.session['token']

            repo_id = request.session['id']
            
            g = Github(token)
            
            repo = g.get_repo(full_name_or_id=int(repo_id))

            repository = Repository.objects.filter(repositoryID=repo.id)
            if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestoneID)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            else:
                save_milestone(repo, repository)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestoneID')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})     

def refresh_milestones(repo, repository, last):
    milestones = repo.get_milestones(state='all')
    for i in range(last+1, milestones.totalCount):
        milestone_model = Milestone.objects.create(repository=repository,
                                                   milestoneID=milestones[i].number,
                                                   state=milestones[i].state,
                                                   title=milestones[i].title,
                                                   author=milestones[i].creator.login,
                                                   created_at=milestones[i].created_at,
                                                   due_on=milestones[i].due_on)
        milestone_model.publish()


def save_milestone(repo, repository):
    for milestone in repo.get_milestones(state='all'):
        milestone_model = Milestone.objects.create(repository=repository,
                                                   milestoneID=milestone.number,
                                                   state=milestone.state,
                                                   title=milestone.title,
                                                   author=milestone.creator.login,
                                                   created_at=milestone.created_at,
                                                   due_on=milestone.due_on)
        milestone_model.publish()

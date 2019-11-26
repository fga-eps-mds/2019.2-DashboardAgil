from django.shortcuts import render
from github import Github
from .models import Repository
from .. import secret
from ..index.models import Usuario
from ..commits.models import Commit
from ..milestone.models import Milestone
from ..issues.models import Issue
from ..pull_requests.models import Pull_request


def repositories(request):

    user_login = secret.login
    password = secret.password
    g = Github(login_or_token=user_login, password=password)
    repos_names = []
    if bool(Repository.objects.filter(user__login=user_login)):
        repos = Repository.objects.filter(user__login=user_login)
        for repository in repos:
            repos_names.append(repository.name)
    else:
        user = Usuario.objects.get(login=user_login)
        for repository in g.get_user().get_repos(type='member'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)
            save_commit(repository, repository_model)
            save_issue(repository, repository_model)
            save_milestone(repository, repository_model)
            save_pull_request(repository, repository_model)
        
        for repository in g.get_user().get_repos(type='owner'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
            repository_model.publish()
            repos_names.append(repository.name)
            save_commit(repository, repository_model)
            save_issue(repository, repository_model)
            save_milestone(repository, repository_model)
            save_pull_request(repository, repository_model)

        for repository in g.get_user().get_repos(type='private'):
            repository_model = Repository.objects.create(user=user,
                                                         name=repository.name,
                                                         repositoryID=repository.id)
           repository_model.publish()
            repos_names.append(repository.name)
            save_commit(repository, repository_model)
            save_issue(repository, repository_model)
            save_milestone(repository, repository_model)
            save_pull_request(repository, repository_model)

    return render(request, 'repositories.html', {'repos': repos_names})


def save_commit(repo, repository):
    for commit in repo.get_commits():
        commit_model = Commit.objects.create(repository=repository,
                                             sha_commit=commit.sha,
                                             author=commit.commit.author.name,
                                             date=commit.commit.author.date)
        commit_model.publish()


def save_issue(repo, repository):
    for issue in repo.get_issues(state='all'):
        issues_model = Issue.objects.create(repository=repository,
                                            issue_number=issue.number,
                                            state=issue.state,
                                            author=issue.user.login,
                                            date=issue.created_at)
        issues_model.publish()


def save_milestone(repo, repository):
    for milestone in repo.get_milestones(state='all'):
        milestone_model = Milestone.objects.create(repository=repository,
                                                   milestoneID=milestone.id,
                                                   state=milestone.state,
                                                   title=milestone.title,
                                                   author=milestone.creator.login,
                                                   created_at=milestone.created_at,
                                                   due_on=milestone.due_on)
        milestone_model.publish()


def save_pull_request(repo, repository):
    for pull_request in repo.get_pulls(state='all'):
        pull_requests_model = Pull_request.objects.create(repository=repository,
                                                          pull_request_number=pull_request.number,
                                                          state=pull_request.state,
                                                          author=pull_request.user.login,
                                                          open_date=pull_request.created_at)
        pull_requests_model.publish()

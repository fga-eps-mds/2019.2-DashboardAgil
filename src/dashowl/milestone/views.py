from django.shortcuts import render
from github import Github



def milestone(request):

    g = Github("joao15victor08", "j15v08o19m99")
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
    milestones = repo.get_milestones()
    totalMilestone = milestone.totalCount


    return render(request, 'milestone.html', {'milestone':milestones, 'total':totalMilestone})

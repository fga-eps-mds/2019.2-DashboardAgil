from django.shortcuts import render
from github import Github



class milestone():  
    def milestone(request):

        g = Github("joao15victor08", "j15v08o19m99")
        repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil")
        milestone = repo.get_milestones()
        totalMilestone = milestone.totalCount


        return render(request, 'milestone.html', {'milestone':milestone , 'total':totalMilestone})

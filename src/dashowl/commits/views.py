from django.shortcuts import render

# Create your views here.
def get_commits(request):

    return render(request,'commits.html',{})
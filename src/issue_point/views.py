from django.shortcuts import render
import requests
import json


#GET /p1/repositories/:repo_id/issues/:issue_number

def open_issue_points(request):

#req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/38?access_token=563259489fc7556b5f4b5cfc0000adba14e89e60eb901883dbf6f8c04f3eaa7e7e3909eb58786850') 
#pontos_issue = req.json()
#print(pontos_issue["estimate"]["value"])


    return render(request,'issue_point.html',{})


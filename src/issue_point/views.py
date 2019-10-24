from django.shortcuts import render
import requests
import json

#GET /p1/repositories/:repo_id/issues/:issue_number


req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=88ecf0f6ad902fa218d3eb2be63b0ff1a4b2f53b3c49aa9493279638612cf7657d22dc87e6892bc3') 

pontos_issue = req.json()

print(pontos_issue["estimate"]["value"])

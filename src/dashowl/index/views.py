from django.shortcuts import render
import requests
from github import Github
from django.contrib.sessions.backends.db import SessionStore

def index (request):

    code  = request.GET["code"]
    r = requests.post("https://github.com/login/oauth/access_token?client_id=1b10677ef95a29f3fdf2&client_secret=9e57bce3d353b44c84f03af3101daa93a1fbb33a&code="+code)

    t = r.text
    token = ""
    for i in range(13,53):
        token += t[i]

    if(token[0].isdigit()):



        g = Github(token)
        user  = g.get_user()
        login = user.login

        s = SessionStore()
        s['login'] = login
        s.create()
        s = SessionStore(session_key = s.session_key)


        

        return render(request, 'index.html', {"token": s['login']})
    
    else:

        return render(request, 'index.html', {})
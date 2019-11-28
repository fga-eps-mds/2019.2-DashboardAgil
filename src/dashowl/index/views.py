from django.shortcuts import render
import requests
from github import Github
from .models import Usuario

def index (request):
    if 'login' not in request.session:
        if request.method == 'GET' and 'code' in request.GET:

            code  = request.GET["code"]

            if code:

                r = requests.post("https://github.com/login/oauth/access_token?client_id=1b10677ef95a29f3fdf2&client_secret=9e57bce3d353b44c84f03af3101daa93a1fbb33a&code="+code)

                t = r.text
                token = ""
                for i in range(13,53):
                    token += t[i]


                if(token[0].isdigit()):



                    g = Github(token)
                    user  = g.get_user()

                    u = Usuario.objects.create(login = user.login)

                    user_login = user.login

                    request.session['login'] = user_login
                    request.session['token'] = token


                    return render(request, 'index.html', {})
                
                else:
                    token_nd = 'nao e digito'
                    return render(request, 'index_s_token.html', {})
            else:
                code_nd = 'code nao existe'
                return render(request, 'index_s_token.html', {})
        else:
            sem_code = 'sem code'
            return render(request, 'index_s_token.html', {})
    else:
        # session_set = 'session seteda'
        return render(request, 'index.html', {})
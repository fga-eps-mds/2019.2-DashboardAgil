
from django.shortcuts import render

# Create your views here.
def milestone(request):
    testando = "Agora foi"
    return render(request, 'milestone.html', {'milestone':testando})
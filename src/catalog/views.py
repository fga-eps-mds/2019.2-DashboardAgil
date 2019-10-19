from django.shortcuts import render

def index(request):


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'charts-chartjs.html')

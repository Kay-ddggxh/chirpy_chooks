from django.shortcuts import render


def index(request):
    """
    renders index page
    """
    return render(request, 'home/index.html')

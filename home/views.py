from django.shortcuts import render

def index(request):
    ''' Index page '''
    return render(request, 'index.html')


def about(request):
    ''' About page '''
    return render(request, 'about.html')


def data(request):
    ''' Data page '''
    return render(request, 'data.html')

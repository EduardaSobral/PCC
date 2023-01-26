from django.shortcuts import render

def index(request):

    print('Está aqui!')

    
    return render(request, '/index.html')
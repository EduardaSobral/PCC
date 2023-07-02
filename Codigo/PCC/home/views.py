from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    is_Gremio = request.user.groups.filter(name='Gremio').exists()

    context = {
        'is_Gremio': is_Gremio
        }
    return render(request, 'home/inicio.html', {})

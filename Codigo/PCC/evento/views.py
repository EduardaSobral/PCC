from imp import new_module
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Cadastro
from evento.form import EventoForm
from datetime import datetime, timedelta, time, date

from .models import Evento

@login_required
def criar(request):

    if request.method == "POST": 
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/evento")
    else: 
        form = EventoForm()

    context = {
        'form': form
    }

    return render(request, 'evento/criar.html/', context)

def index(request):
    
    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    evento = Evento.objects.all()
    
    context = {
        'evento': evento,
        'is_Gremio': is_Gremio
    }

    return render(request, 'evento/index.html', context)

#método para detalhar evento

def detail(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    context = {
        'evento': evento
    }

    return render(request, 'evento/detail.html', context)

@login_required
def editar(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/evento")
    else:    
        form = EventoForm(instance=evento)
    
    context = {
        'form': form,
        'evento_id': evento_id,
    }
    
    return render(request, 'evento/editar.html', context)

@login_required
def excluir(request, evento_id):
    
    Evento.objects.get(pk=evento_id).delete()
    
    return HttpResponseRedirect("/evento")


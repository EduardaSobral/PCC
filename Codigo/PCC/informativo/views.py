from django.shortcuts import render
from .form import InformativoForm
from .models import Informativo
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):

    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    informativo = Informativo.objects.all()

    context = {
        'informativo': informativo,
        'is_Gremio': is_Gremio
        }
    
    return render(request, 'informativo/index.html', context)

def detail(request, informativo_id):
    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    informativo = Informativo.objects.get(pk=informativo_id)
    context = {
        'informativo': informativo,
        'is_Gremio': is_Gremio
    }

    return render(request, 'informativo/detail.html', context)

#método para excluir uma informativo
@login_required
def excluir(request, informativo_id):

    Informativo.objects.get(pk=informativo_id).delete()
    
    return HttpResponseRedirect("/informativo")

#método para criar uma nova informativo
@login_required
def criar(request):
    
    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    if request.method == "POST": 
        form = InformativoForm(request.POST)

        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/informativo")
    else: 
        form = InformativoForm()

    context = {
        'form': form,
        'is_Gremio': is_Gremio
    }

    return render(request, 'informativo/criar.html/', context)

#método para editar um registro de informativo
@login_required
def editar(request, informativo_id):
    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    informativo = Informativo.objects.get(pk=informativo_id)

    if request.method == "POST":
        form = InformativoForm(request.POST, instance=informativo)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/informativo")
    else:
        form = InformativoForm(instance=informativo)

    context = {
        'form': form,
        'informativo_id': informativo_id,
        'is_Gremio': is_Gremio
    }

    return render(request, 'informativo/editar.html', context)
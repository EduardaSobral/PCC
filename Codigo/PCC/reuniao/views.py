from django.shortcuts import render
from .form import ReuniaoForm
from .models import Reuniao
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    print('Está aqui!')
    reuniao = Reuniao.objects.all()
    is_Gremio = request.user.groups.filter(name='Gremio').exists()

    context = {
        'is_Gremio': is_Gremio,
        'reuniao': reuniao,
    }
    
    return render(request, 'reuniao/index.html', context)

@login_required
def detail(request, reuniao_id):
    reuniao = Reuniao.objects.get(pk=reuniao_id)
    context = {
        'reuniao': reuniao
    }

    return render(request, 'reuniao/detail.html', context)

#método para excluir uma reuniao
@login_required
def excluir(request, reuniao_id):

    Reuniao.objects.get(pk=reuniao_id).delete()
    
    return HttpResponseRedirect("/reuniao")

#método para criar uma nova reuniao
@login_required
def criar(request):

    if request.method == "POST": 
        form = ReuniaoForm(request.POST)

        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/reuniao")
    else: 
        form = ReuniaoForm()

    context = {
        'form': form
    }

    return render(request, 'reuniao/criar.html/', context)

#método para editar um registro de reuniao
@login_required
def editar(request, reuniao_id):
    reuniao = Reuniao.objects.get(pk=reuniao_id)

    if request.method == "POST":
        form = ReuniaoForm(request.POST, instance=reuniao)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/reuniao")
    else:
        form = ReuniaoForm(instance=reuniao)

    context = {
        'form': form,
        'reuniao_id': reuniao_id
    }

    return render(request, 'reuniao/editar.html', context)
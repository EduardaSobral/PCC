from django.shortcuts import render
from accounts.form import CadastroForm
from .models import Cadastro
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def register(request):
    
    if request.method == "POST":
        form = CadastroForm(request.POST) 
        if form.is_valid():
            new_user = form.save(commit=False)

            form.save()            
            
            group = Group.objects.get(name='Gremio')
            new_user.groups.add(group) 
            return HttpResponseRedirect("/accounts/login/")
    else:    
        form = CadastroForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'registration/register.html', context)

def password(request):
    
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            
            form.save()            
            return HttpResponseRedirect("/accounts/login/")
    else:    
        form = CadastroForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'registration/password.html', context)


# Parte dos contatos


def index(request):
    
    is_Gremio = request.user.groups.filter(name='Gremio').exists()
    contato = Cadastro.objects.all()
    
    context = {
        'contato': contato,
        'is_Gremio': is_Gremio
    }

    return render(request, 'contato/index.html', context)


@login_required
def excluir(request, contato_id):
    
    Cadastro.objects.get(pk=contato_id).delete()
    
    return HttpResponseRedirect("/contato")
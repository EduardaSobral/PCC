from django.shortcuts import render
from accounts.form import CadastroForm
from .models import Cadastro
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

def register(request):
    
    if request.method == "POST":
        form = CadastroForm(request.POST) 
        if form.is_valid():
            new_user = form.save(commit=False)

            form.save()            
            
            group = Group.objects.get(name='Alunos')
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



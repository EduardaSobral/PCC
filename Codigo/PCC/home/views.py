from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, 'home/inicio.html', {})

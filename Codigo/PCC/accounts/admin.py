from atexit import register
from django.contrib import admin

from .models import Cadastro

admin.site.register(Cadastro)
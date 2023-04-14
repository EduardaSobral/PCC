from django.urls import path

from . import views

urlpatterns = [
    path('criar/', views.criar, name='criar'),
    path('', views.index, name='index'),
    path('<int:informativo_id>/', views.detail, name='detail'),
    path('editar/<int:informativo_id>/', views.editar, name='editar'),
    path('excluir/<int:informativo_id>/', views.excluir, name='excluir'),
]
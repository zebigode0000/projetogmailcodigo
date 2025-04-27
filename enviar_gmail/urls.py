from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('criar/', views.criar_projeto, name='criar_projeto'),
    path('excluir/<int:projeto_id>/', views.solicitar_exclusao, name='solicitar_exclusao'),
    path('confirmar-exclusao/', views.confirmar_exclusao, name='confirmar_exclusao'),
]

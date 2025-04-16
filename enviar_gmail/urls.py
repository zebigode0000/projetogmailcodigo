from django.urls import path
from . import views

urlpatterns = [
    path('excluir/', views.excluir_pedido, name='excluir'),
    path('verificar/', views.verificar_codigo, name='verificar_codigo'),
]

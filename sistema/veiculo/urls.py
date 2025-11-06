from django.shortcuts import render, redirect
from django.urls import path
from .views import CriarVeiculos, ListarVeiculos, FotoVeiculo, EditarVeiculo, ExcluirVeiculo, APIListarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('editar/<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path('excluir/<int:pk>/', ExcluirVeiculo.as_view(), name='excluir-veiculo'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='fotos-veiculos'),
    # API endpoint moved here so it is available under /veiculo/api/
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculo'),
]
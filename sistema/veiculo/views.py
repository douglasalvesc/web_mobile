# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self):
        data_atual = datetime.now()
        return Veiculo.objects.all()
    
class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para a criação de veiculos
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    #success_url = '/veiculo' ou
    success_url = reverse_lazy('listar-veiculos') #prova: porque essa linha é melhor?
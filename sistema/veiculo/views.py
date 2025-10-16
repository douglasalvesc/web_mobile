# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, UpdateView, DeleteView
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

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

    def form_valid(self, form):
        form.instance.proprietario = self.request.user
        return super().form_valid(form)

class FotoVeiculo(View):
    """
    View para retornar a foto do veículos
    """

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto=f'veiculo/fotos/{arquivo}')
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado!")
        except Exception as exception:
            raise exception

class EditarVeiculo(LoginRequiredMixin, UpdateView):
    """
    View para a edição de veículos
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class ExcluirVeiculo(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão de veículos
    """
    model = Veiculo
    template_name = 'veiculo/veiculo_confirm_delete.html'
    success_url = reverse_lazy('listar-veiculos')
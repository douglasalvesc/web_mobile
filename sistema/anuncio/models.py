from django.db import models
from django.contrib.auth.models import User
from veiculo.models import Veiculo

class Anuncio(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='anuncios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Anúncio de {self.veiculo.modelo} por {self.usuario.username}"

    class Meta:
        ordering = ['-data_criacao']

from django.db import models
from django.contrib.auth.models import User
from veiculo.consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS

class Veiculo(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='veiculos', default=1)
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')

    def __str__(self):
        return f'{self.get_marca_display()} {self.modelo} ({self.ano})'
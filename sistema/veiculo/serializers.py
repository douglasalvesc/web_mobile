from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para o model de veículos
    """

    class Meta:
        model = Veiculo
        exclude = []
        
    def get_nome_marca(self, instancia):
        return instancia.get_marca_display()
    
    def get_nome_cor(self, instancia):
        return instancia.get_marca_display()
    
    def get_nome_combustivel(self, instancia):
        return instancia.get_marca_display()
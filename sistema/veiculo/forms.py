from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):
    """
    Formulario para o model Veiculo
    """
    class Meta:
        model = Veiculo
        exclude = ['proprietario']
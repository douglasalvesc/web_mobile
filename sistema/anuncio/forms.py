from django import forms
from .models import Anuncio
from veiculo.models import Veiculo

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['veiculo', 'valor', 'descricao']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AnuncioForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['veiculo'].queryset = Veiculo.objects.filter(proprietario=user)
        
        self.fields['valor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ex: 50000.00'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Adicione detalhes sobre o veículo ou o anúncio...'})

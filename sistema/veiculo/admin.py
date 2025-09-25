from django.contrib import admin
from veiculo.models import Veiculo

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'ano', 'cor', 'combustivel']
    list_filter = ['marca', 'ano', 'cor', 'combustivel']
    search_fields = ['modelo']
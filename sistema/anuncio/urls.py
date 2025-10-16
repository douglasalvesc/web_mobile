from django.urls import path
from .views import AnuncioListView, AnuncioCreateView, AnuncioUpdateView, AnuncioDeleteView, MeusAnunciosListView

urlpatterns = [
    path('', AnuncioListView.as_view(), name='listar-anuncios'),
    path('meus-anuncios/', MeusAnunciosListView.as_view(), name='meus-anuncios'),
    path('novo/', AnuncioCreateView.as_view(), name='criar-anuncio'),
    path('editar/<int:pk>/', AnuncioUpdateView.as_view(), name='editar-anuncio'),
    path('excluir/<int:pk>/', AnuncioDeleteView.as_view(), name='excluir-anuncio'),
]

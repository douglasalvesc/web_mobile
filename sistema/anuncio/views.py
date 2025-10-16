from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Anuncio
from .forms import AnuncioForm

class AnuncioListView(ListView):
    model = Anuncio
    template_name = 'anuncio/listar.html'
    context_object_name = 'anuncios'
    paginate_by = 10

    def get_queryset(self):
        return Anuncio.objects.filter(ativo=True).select_related('veiculo', 'usuario')

class MeusAnunciosListView(LoginRequiredMixin, ListView):
    model = Anuncio
    template_name = 'anuncio/meus_anuncios.html'
    context_object_name = 'anuncios'
    paginate_by = 10

    def get_queryset(self):
        return Anuncio.objects.filter(usuario=self.request.user).select_related('veiculo', 'usuario')

class AnuncioCreateView(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('meus-anuncios')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AnuncioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('meus-anuncios')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        anuncio = self.get_object()
        return self.request.user == anuncio.usuario

class AnuncioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/anuncio_confirm_delete.html'
    success_url = reverse_lazy('meus-anuncios')

    def test_func(self):
        anuncio = self.get_object()
        return self.request.user == anuncio.usuario

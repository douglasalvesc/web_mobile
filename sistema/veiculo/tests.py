from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
    '''
    Classe de testes para o modelo Veiculo.
    '''
    def setUp(self):
        self.instancia = Veiculo.objects.create(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )

    def test_is_new(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)

    def test_years_of_use(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculo(TestCase):
    '''
    Classe de testes para a view listar_veiculos.
    '''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('listar-veiculos')
        Veiculo.objects.create(marca=1, modelo='Modelo1', ano=2020, cor=2, combustivel=3)
        Veiculo.objects.create(marca=2, modelo='Modelo2', ano=2, cor=3, combustivel=1)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['lista_veiculos']), 2)

class TestesViewCriarVeiculos(TestCase):
    '''
    Classe de testes para a view criar_veiculo.
    '''
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculos')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], FormularioVeiculo)

    def test_post(self):
        data = {
            'marca': 1,
            'modelo': 'TesteModelo',
            'ano': 2021,
            'cor': 2,
            'combustivel': 3
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'TesteModelo')

class TestesViewEditarVeiculos(TestCase):
    '''
    Classe de testes para a view editar_veiculo.
    '''
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.veiculo = Veiculo.objects.create(marca=1, modelo='ModeloOriginal', ano=2020, cor=2, combustivel=3)
        self.url = reverse('editar-veiculos', kwargs={'pk': self.veiculo.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.veiculo.pk)
        self.assertEqual(response.context.get('object').marca, 1)

    def test_post(self):
        data = {
            'marca': 2,
            'modelo': 'ModeloEditado',
            'ano': 2021,
            'cor': 3,
            'combustivel': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 2)
        self.assertEqual(Veiculo.objects.first().pk, self.veiculo.pk)

class TestesViewDeletarVeiculos(TestCase):
    '''
    Classe de testes para a view deletar_veiculo.
    '''
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='ModeloParaDeletar', ano=2020, cor=2, combustivel=3)
        self.url = reverse('deletar-veiculos', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)
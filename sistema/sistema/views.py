from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Login(View):
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('username', None)
        senha = request.POST.get('password', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponse('Usuario autenticado com sucesso!')
            #return redirect("/veiculos")
        return render(request, 'autenticacao.html', {"error": "Usuário ou senha inválidos!"})
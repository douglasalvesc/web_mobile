from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render, redirect

class Login(View):
    def get(self, request):
        contexto = {}
        if request.user.is_authenticated:
            return redirect("/veiculo")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('username', None)
        senha = request.POST.get('password', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect("/veiculo")
        return render(request, 'autenticacao.html', {"error": "Usuário ou senha inválidos!"})
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
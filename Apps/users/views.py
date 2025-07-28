# users/views.py

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        error = None
        success = None
        username = request.POST.get('username')
        email    = request.POST.get('email')
        p1       = request.POST.get('password1')
        p2       = request.POST.get('password2')

        if not username or not email or not p1 or not p2:
            error = 'Preencha todos os campos.'
        elif p1 != p2:
            error = 'As senhas não coincidem.'
        elif len(p1) < 6:
            error = 'A senha deve ter pelo menos 6 caracteres.'
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=p1)
                user.save()
                success = 'Usuário criado com sucesso! Faça login.'
            except IntegrityError:
                error = 'Nome de usuário ou e-mail já cadastrado.'

        return render(request, self.template_name, {
            'error':   error,
            'success': success,
        })


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        error = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')  # ou dashboard
        else:
            error = 'Usuário ou senha inválidos.'
        return render(request, self.template_name, {'error': error})

from django.contrib.auth.models import User
from django.db import IntegrityError

def register_view(request):
    error = None
    success = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not username or not email or not password1 or not password2:
            error = 'Preencha todos os campos.'
        elif password1 != password2:
            error = 'As senhas não coincidem.'
        elif len(password1) < 6:
            error = 'A senha deve ter pelo menos 6 caracteres.'
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                success = 'Usuário criado com sucesso! Faça login.'
            except IntegrityError:
                error = 'Nome de usuário ou e-mail já cadastrado.'
    return render(request, 'users/register.html', {'error': error, 'success': success})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse

def login_view(request: HttpRequest) -> HttpResponse:
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redireciona para a home ou dashboard
        else:
            error = 'Usuário ou senha inválidos.'
    return render(request, 'users/login.html', {'error': error})

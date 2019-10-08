from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, EditConta
from django.contrib.auth.decorators import login_required
from cursos.models import Curso

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('/')
        else:
            usuario_incorreto = True
            return render(request, 'login.html', {'usuario_incorreto': usuario_incorreto})
    return render(request, 'login.html')


def do_logout(request):
    logout(request)
    return redirect('/')


def RegistrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = CustomUserCreationForm()
    context={
        'cursos': Curso.objects.all(),
        'forms': form
    }
    return render(request, 'cadastro.html', context)


@login_required(login_url='/contas/login')
def painel_de_usuarios(request):
    return render(request, 'painel-de-usuarios.html')


@login_required(login_url='/contas/login')
def editar_conta(request):
    context = {}
    if request.method == 'POST':
        form = EditConta(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditConta(instance=request.user)
            context['success'] = True
    else:
        form = EditConta(instance=request.user)
    context['form'] = form
    return render(request, 'editar_conta.html', context)


@login_required(login_url='/contas/login')
def editar_seguranca(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, 'editar_seguranca.html', context)
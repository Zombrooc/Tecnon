from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Curso, Paragrafo
from .forms import CommentForm


@login_required(login_url='/contas/login')
def cursos(request):
	cursos = Curso.objects.all()
	return render(request, 'cursos.html', {'cursos': cursos})


@login_required(login_url='/contas/login')
def detalhe(request, slug):
	cursos = get_object_or_404(Curso, slug=slug)
	context = {
		'cursos': cursos,
		'postagens': cursos.postagem.all(),
		'range': range(0+1, cursos.n_modulos+1)
	}
	return render(request, 'detalhe.html', context)


@login_required(login_url='/contas/login')
def show_posts(request, slug, slug2):
	curso = get_object_or_404(Curso, slug=slug)
	postagem = get_object_or_404(curso.postagem.all(), slug=slug2)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.postagem = postagem
			comment.save()
			return redirect('show_posts', slug)
	else:
		form = CommentForm()
	context={
		'curso': curso,
		'postagem': postagem,
		'paragrafos': postagem.paragrafo.all(),
		'form': form
	}

	return render(request, 'postagem.html', context)
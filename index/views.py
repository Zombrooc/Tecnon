from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from cursos.models import Postagem

#from .models import Atualizacao

from datetime import datetime, timedelta

# Create your views here.
def home(request):
	three_days_ago = datetime.now() - timedelta(days=3)
	postagens = Postagem.objects.all().filter(created_at__gte=three_days_ago)
	#atualizacoes = Atualizacao.objects.all()
	context = {
		'postagens': postagens,
		#'atualizacoes': atualizacoes

	}
	return render(request, 'home.html', context)


def base(request):
	return render(request, 'base.html')


def contato(request):
	return render(request, 'contato.html')


def sobre(request):
	return render(request, 'sobre.html')


def google(request):
	return render(request, 'googlefb3c6a4443b4ed52.html')


def robots(request):
	return render(request, 'robots.txt')


def sitemap(request):
	return render(request, 'sitemap.xml')


def show_att(request, slug):
	att = get_object_or_404(Atualizacao, slug=slug)
	return render(request, 'atualizacoes.html', {'atualizacao': att})
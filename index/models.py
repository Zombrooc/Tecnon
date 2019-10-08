from django.db import models
from django.urls import reverse
from .views import show_att


class Atualizacao(models.Model):
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    versao = models.CharField('Versão', max_length=100)
    conteudo = models.TextField('Conteúdo', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


    def __str__(self):
        return self.titulo

 
    def get_absolute_url(self):
        return reverse('show_att', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'Atualização'
        verbose_name_plural = 'Atualizações'
        ordering = ['-created_at']
from django.db import models
from django.urls import reverse
from django.conf import settings


class CursoManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    slug = models.SlugField('Atalho')
    duracao = models.CharField(max_length=100)
    n_modulos = models.IntegerField()
    turnos = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CursoManager()

    def __str__(self):
        return self.nome_curso
    

    def get_absolute_url(self):
        return reverse('detalhe', kwargs={'slug': self.slug})


class Postagem(models.Model):
    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        on_delete=models.CASCADE,
        related_name='postagem'
    )
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    modulo = models.IntegerField(blank=True, null=True)
    disciplina = models.CharField('Disciplina', max_length=50, null=True, blank=True)
    prof = models.CharField('Professor(a)', max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='postagem/images', verbose_name="Imagem", null=True, blank=True)


    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


    def __str__(self):
        return self.titulo

    
    def get_absolute_url(self):
        return reverse('show_posts', kwargs={'slug': self.curso.slug, 'slug2': self.slug})


    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-created_at']


class Paragrafo(models.Model):
    postagem = models.ForeignKey(
        Postagem,
        verbose_name = 'Postagem',
        on_delete = models.CASCADE,
        related_name = 'paragrafo'
    )

    titulo = models.CharField('Titulo', max_length=200, blank=True)
    conteudo = models.TextField('Conteúdo', blank=True)
    imagem = models.ImageField(upload_to='paragrafo/images', verbose_name="Imagem", null=True, blank=True)


    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


    def __str__(self):
        return self.titulo 


    class Meta:
        verbose_name = 'Parágrafo'
        verbose_name_plural = 'Parágrafos'
        ordering = ['created_at']


class Comment(models.Model):
    postagem = models.ForeignKey(
        Postagem,
        verbose_name='Postagem',
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name = 'username',
        on_delete=models.CASCADE
    )
    comment = models.TextField('Comentário')


    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


    def __str__(self):
        return self.comment


    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['created_at']

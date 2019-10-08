from django.contrib import admin
from .models import Curso, Postagem, Comment, Paragrafo


class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('nome_curso',)}


class ParagrafoAdmin(admin.TabularInline):
    model = Paragrafo


class PostagemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ['curso', 'titulo', 'modulo','disciplina', 'created_at']
	search_fields = ['curso', 'titulo', 'disciplina']
	list_filter = ['curso', 'titulo', 'disciplina', 'created_at']


	inlines = [
		ParagrafoAdmin	
	]


class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'postagem']
	list_filter = ['postagem', 'created_at']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Curso, CursosAdmin)
admin.site.register(Postagem, PostagemAdmin)


from django.contrib import admin
from .models import Atualizacao


class AttAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('titulo',)}



admin.site.register(Atualizacao, AttAdmin)

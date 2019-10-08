from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm, EditConta
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = EditConta
    model = User
    list_display = ('username', 'nome', 'sobrenome','is_superuser', 'is_staff', 'created_at')
    list_filter = ('nome', 'sobrenome', 'is_superuser', 'is_staff')
    exclude = ('password',)

admin.site.register(User, CustomUserAdmin)
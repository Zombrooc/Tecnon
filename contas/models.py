from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from cursos.models import Curso


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        kwargs.pop("password")

        if not username:
            raise ValueError(_('Digite um nome de usuário'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


OPCAO = (
    ('informatica', 'Informática'),
    ('recursos-humanos', 'Recursos Humanos'),
    ('logistica', 'Logística'),
    ('magisterio', 'Magistério'),
    ('administracao', 'Administração')
)


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(

        'Username',
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        'Nome',
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Sobrenome',
        max_length=50,
        blank=True,
        null=True
    )
    curso = models.CharField(
        'Curso',
        max_length=200,
        choices=OPCAO,
        blank=True,
        null=True
    )
    email = models.EmailField(
        'E-mail',
        max_length=50,
        unique=True,
        blank = False,
        null=False,
        default="admin@admin.com"
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)



    is_superuser = models.BooleanField('Superuser', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    is_admin = models.BooleanField('Admin', default=False)
    is_staff = models.BooleanField('Equipe', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = EmailUserManager()



    def __str__(self):
        return self.username


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

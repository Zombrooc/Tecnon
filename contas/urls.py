from django.conf.urls import url
from contas.views import login_view, do_logout, RegistrationView, painel_de_usuarios, editar_conta, editar_seguranca


urlpatterns = [
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', do_logout, name="logout"),
    url(r'^cadastrar/$', RegistrationView, name="cadastro"),
    url(r'^$', painel_de_usuarios, name='painel_de_usuarios'),
    url(r'^editar-conta/$', editar_conta, name='editar_conta'),
    url(r'^editar-seguranca/$', editar_seguranca, name='editar_seguranca')
]
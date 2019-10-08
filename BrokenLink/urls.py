from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


from index.views import home, base, contato, sobre, google, robots, sitemap
from conversor_de_base.views import Conversor_de_Base
from gerador_cpf.views import gerador_cpf
from calc_ip.views import calc_ip
from cursos.views import cursos
# from contas.views import login_view, logout_view, RegistrationView
from contas.views import login_view, do_logout, RegistrationView
from index.views import show_att


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^ferramentas/conversor-de-bases/', Conversor_de_Base, name='conversor-de-bases'),
    url(r'^ferramentas/gerador-de-cpf/', gerador_cpf, name='gerador_cpf'),
    url(r'^ferramentas/calculadora-ip/', calc_ip, name='calculadora_ip'),
    url(r'^googlefb3c6a4443b4ed52.html/', google, name='google'),
    url(r'^cursos/', include('cursos.urls')),
    url(r'^base/', base, name='base'),
    url(r'^contas/', include('contas.urls')),
    url(r'^contato/', contato, name='contato'),
    url(r'^sobre/', sobre, name='sobre'),
    url(r'^robots.txt$', robots, name='robots'),
    url(r'^sitemap.xml$', sitemap, name='sitemap'),
    url(r'^(?P<slug>[\w_-]+)/$', show_att, name='show_att'),
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
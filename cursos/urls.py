from django.conf.urls import url
from django.urls import include


from cursos.views import cursos, detalhe, show_posts


urlpatterns = [
    url(r'^$', cursos, name='cursos'),
    url(r'^(?P<slug>[\w_-]+)/$', detalhe, name='detalhe'),
    #url(r'^(?P<slug>[\w_-]+)/(?P<pk>\d+)/$', show_posts, name='show_posts')
    url(r'^(?P<slug>[\w_-]+)/(?P<slug2>[\w_-]+)/$', show_posts, name='show_posts')
]

"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^history$', 'history', name='history'),
    url(r'^news$', 'news', name='news'),
    url(r'^hotels$', 'hotels', name='hotels'),
)

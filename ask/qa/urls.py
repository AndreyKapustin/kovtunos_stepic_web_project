from django.conf.urls import patterns, include, url
from django.contrib import admin
from qa.views import test, question_list, question_detail

urlpatterns = patterns('',
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^admin/', admin.site.urls),
)

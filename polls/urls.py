##from django.conf.urls import patterns, url

from django.conf.urls import patterns, include, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    ####################################################
    #url(r'^home$', views.home1, name='home'),
    url(r'^$', 'polls.views.home1', name='home'),
    url(r'^geo$','polls.views.indexx', name='indexx'),
    url(r'^kenn$','polls.views.kenn', name='kenn'),
    url(r'^error$','polls.views.error', name='error'),
   #####################################################
   
    url(r'^render$', 'polls.views.home', name='home'),
    url(r'^info/$', 'polls.views.info', name='info'),
    url(r'^mapget/$', 'polls.views.get_apartments', name='get-apartment'),
    url(r'^mapapart/$', 'polls.views.apartments_filter', name='apartments_filter'),

    
   
                       
)

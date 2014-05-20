from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    ####################################################
    url(r'^$', views.home, name='home'),
    url(r'^geo$','polls.views.indexx', name='indexx'),
    url(r'^kenn$','polls.views.kenn', name='kenn'),
    url(r'^error$','polls.views.error', name='error'),
   #####################################################                    
    
              
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/votehax/$', views.vote, name='votex'),
                       
)

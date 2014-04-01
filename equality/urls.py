
from django.conf.urls import patterns, url

from equality import views

urlpatterns = patterns('',
    # ex: /equality/
    url(r'^$', views.weather_chart_view, name='weather_chart_view'),
)


####from django.conf.urls import patterns, include, url
#### 
####urlpatterns = patterns('equality.views',
####    url(r'^$', 'weather_chart_view'),
####)

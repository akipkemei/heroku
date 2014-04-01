from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from equality.models import MonthlyWeatherByCity

import os.path
from Cheetah.Template import Template
from django.conf import settings
#from django.http import HttpResponse
def render_to_response(template_name, context, **kwargs):
    for template_dir in settings.TEMPLATE_DIRS:
        path = os.path.join(template_dir, template_name)
        if os.path.exists(path):
            template = Template(file = path, searchList = (context,))
            return HttpResponse(unicode(template), **kwargs)
    raise ValueError, 'Could not find template for %s' % template_name

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

###########################
from django.shortcuts import render_to_response
 
from chartit import DataPool, Chart
 
from models import MonthlyWeatherByCity
 
def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])
 
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})
 
    #Step 3: Send the chart object to the template.
    return render_to_response('equality/weather.html', {'weatherchart': cht})


##
##def index(request):
##    latest_poll_list = Poll.objects.all()
##    latest_poll_list1 = MonthlyWeatherByCity.objects.all()
##    latest_poll_list3 = Poll.objects.all().order_by('-pub_date')[:5]
##    context = {'latest_poll_list1': latest_poll_list1,'latest_poll_list': latest_poll_list,'latest_poll_list3': latest_poll_list3}
##    return render_to_response('polls/inndex.tmpl', context)


##def index(request):
##    latest_poll_list1 = MonthlyWeatherByCity.objects.all() 
##    context = {'latest_poll_list1': latest_poll_list1}
##    return render_to_response('polls/inndex.tmpl', context)

######from chartit import DataPool, Chart
######
######def weather_chart_view(request):
######    #Step 1: Create a DataPool with the data we want to retrieve.
######    weatherdata = \
######        DataPool(
######           series=
######            [{'options': {
######               'source': MonthlyWeatherByCity.objects.all()},
######              'terms': [
######                'month',
######                'houston_temp',
######                'boston_temp']}
######             ])
######
######    #Step 2: Create the Chart object
######    cht = Chart(
######            datasource = weatherdata,
######            series_options =
######              [{'options':{
######                  'type': 'line',
######                  'stacking': False},
######                'terms':{
######                  'month': [
######                    'boston_temp',
######                    'houston_temp']
######                  }}],
######            chart_options =
######              {'title': {
######                   'text': 'Weather Data of Boston and Houston'},
######               'xAxis': {
######                    'title': {
######                       'text': 'Month number'}}})
######
######    #Step 3: Send the chart object to the template.
######    return render_to_response('equity/weatherchart.html',{'weatherchart': cht})

#################

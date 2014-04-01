from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from equality.models import MonthlyWeatherByCity

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

############################
##def toJSON(obj):
##   if isinstance(obj, QuerySet):
##       return simplejson.dumps(obj, cls=DjangoJSONEncoder)
##   if isinstance(obj, models.Model):
##       #do the same as above by making it a queryset first
##       set_obj = [obj]
##       set_str = simplejson.dumps(simplejson.loads(serialize('json', set_obj)))
##       #eliminate brackets in the beginning and the end 
##       str_obj = set_str[1:len(set_str)-2]
##   return str_obj


###########################
 
from chartit import DataPool, Chart
 
from models import MonthlyWeatherByCity

###########################


from chartit import DataPool, Chart
from chartit import DataPool, Chart

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
    return render_to_response( 'equality/weather.html', {'weatherchart': cht})

###############################
 
####def weather_chart_view(request):
####    #Step 1: Create a DataPool with the data we want to retrieve.
####    weatherdata = \
####        DataPool(
####           series=
####            [{'options': {
####               'source': MonthlyWeatherByCity.objects.all()},
####              'terms': [
####                'month',
####                'houston_temp',
####                'boston_temp']}
####             ])
#### 
####    #Step 2: Create the Chart object
####    cht = Chart(
####            datasource = weatherdata,
####            series_options =
####              [{'options':{
####                  'type': 'line',
####                  'stacking': False},
####                'terms':{
####                  'month': [
####                    'boston_temp',
####                    'houston_temp']
####                  }}],
####            chart_options =
####              {'title': {
####                   'text': 'Weather Data of Boston and Houston'},
####               'xAxis': {
####                    'title': {
####                       'text': 'Month number'}}})
####    context = {'cht': cht}
#### 
####    #Step 3: Send the chart object to the template.
####    ##return render_to_response('equality/weather.html', {'weatherchart': cht})
####    return render(request, 'equality/weather.html', context)


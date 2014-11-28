#from django.shortcuts import render
from django.http import Http404
#from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from equality.models import MonthlyWeatherByCity
from equality.models import DailyWeather



#from django.template import Context, loader
from django.db.models import Avg

from django.shortcuts import render_to_response

###########################


##########################


from chartit import DataPool,Chart






##def weather_chart_view(request):
##    #Step 1: Create a DataPool with the data we want to retrieve.
##    weatherdata = \
##        DataPool(
##           series=
##            [{'options': {
##               'source': MonthlyWeatherByCity.objects.all()},
##              'terms': [
##                'month',
##                'houston_temp',
##                'boston_temp']}
##             ])
##
##    #Step 2: Create the Chart object
##    cht = Chart(
##            datasource = weatherdata,
##            series_options =
##              [{'options':{
##                  'type': 'line',
##                  'stacking': False},
##                'terms':{
##                  'month': [
##                    'boston_temp',
##                    'houston_temp']
##                  }}],
##            chart_options =
##              {'title': {
##                   'text': 'Weather Data of Boston and Houston'},
##               'xAxis': {
##                    'title': {
##                       'text': 'Month number'}}})
##
##    #Step 3: Send the chart object to the template.
##    return render_to_response( 'equality/weather.html', {'weatherchart': cht})

#########################

def monthname(month_num):
    names ={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'August', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return names[month_num]

###############################
 
from chartit import PivotDataPool, PivotChart

def rainfall_pivot_chart_view(request):
    #Step 1: Create a PivotDataPool with the data we want to retrieve.
    rainpivotdata = \
        PivotDataPool(
           series =
            [{'options': {
               'source': DailyWeather.objects.all(),
               'categories': ['month']},
              'terms': {
                'avg_rain': Avg('rainfall'),
##                'legend_by': ['city'],
##                'top_n_per_cat': 3
                }}
             ])

    #Step 2: Create the PivotChart object
    vcht = \
        PivotChart(
            datasource = rainpivotdata,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': True},
                'terms':[
                  'avg_rain']}],
            chart_options =
              {'title': {
                   'text': 'Rain by Month in top 3 cities'},
               'xAxis': {
                    'title': {
                       'text': 'Month'}}})

#########################################
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
    cht1 = Chart(
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
#########################################################################################
#########################################################################################
#########################################################################################
    
    ds = DataPool(
       series=
        [{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
          'terms': [
            'month',
            'boston_temp']}
         ])
##    def monthname(month_num):
##        names ={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
##            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
##    return names[month_num]

    pcht = Chart(
        datasource = ds, 
        series_options = 
          [{'options':{
              'type': 'pie',
              'stacking': False},
            'terms':{
              'month': [
                'boston_temp']
              }}],
        chart_options = 
          {'title': {
               'text': 'Monthly Temperature of Boston'}},
        x_sortf_mapf_mts = (None, monthname, False))
    ######    ######    ######    ######    ######    ######    ######    ######
    dis = DataPool(
       series=
        [{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
          'terms': [
            'month', 
            'boston_temp',
            'houston_temp']}
         ])


    mcht = Chart(
            datasource = dis, 
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': True},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }},
            

               {'options':{
                  'type': 'pie',
                  'center': [100, 20],
                  'size': '50%'},
                'terms':{
                  'month': [
                    'houston_temp']
                  }}
               ],
            
            chart_options = 
              {'title': {
                   'text': 'Weather Data of Boston (line) and Houston (pie)'}},
            x_sortf_mapf_mts = [(None, monthname, False),
                                (None, monthname, False)])
    #######    ######    ######    ######    ######    ######    ######    ######
    ycht = Chart(
        datasource = dis, 
        series_options = 
          [{'options':{
              'type': 'column',
              'stacking': True},
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
    ######
   
    
    rainpivchart = {'rainpivchart': [cht,cht1,vcht,pcht,mcht,ycht]}
    
   
 #   rainpivchart = {'rainpivchart':[rainpivcht, cht]}
 

    #Step 3: Send the PivotChart object to the template.
    return render_to_response('equality/weather.html', rainpivchart)
######################################################################
###################################



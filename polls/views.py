from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader



from polls.models import Poll
#from equality.models import MonthlyWeatherByCity

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



##def index(request):
##    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
##    output = ', '.join([p.question for p in latest_poll_list])
##    return HttpResponse(output)

##
####def index(request):
####    latest_poll_list = Poll.objects.all()
####    template = loader.get_template('polls/inndex.tmpl')
####    context = RequestContext(request, {'latest_poll_list': latest_poll_list,})
####    return HttpResponse(template.render(context))

####



def index(request):
    latest_poll_list = Poll.objects.all()
    latest_poll_list1 = MonthlyWeatherByCity.objects.all()
    latest_poll_list3 = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list1': latest_poll_list1,'latest_poll_list': latest_poll_list,'latest_poll_list3': latest_poll_list3}
    return render_to_response('polls/inndex.tmpl', context)


##def index(request):
##    latest_poll_list1 = MonthlyWeatherByCity.objects.all() 
##    context = {'latest_poll_list1': latest_poll_list1}
##    return render_to_response('polls/inndex.tmpl', context)

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
    return render_to_response({'equity/weatherchart.html': cht})

##def index(request):
##    latest_poll_list = MonthlyWeatherByCity.objects.all()
##    context = {'latest_poll_list': latest_poll_list}
##    return render_to_response('polls/inndex.tmpl', context)
####
##def index(request):
##    latest_poll_list = Poll.objects.all()
##    context = {'latest_poll_lists': latest_poll_list}
##    return render(request, 'polls/inndex.tmpl', context)

##def index(request):
##    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:len(Poll.objects.all())]
##    context = {'latest_poll_lists': latest_poll_list}
##    return render(request, 'polls/inndex.html', context)

##
##def detail(request, poll_id):
##    return HttpResponse("You're looking at poll %s." % poll_id)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

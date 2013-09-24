from django.http import HttpResponse
#from django.template import Context
#from django.template.loader import get_template
from django.shortcuts import render
import datetime

def base(request):
    return render(request,'base.html')

def hello(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except:
        ua = 'unknown'
    #return HttpResponse("Your browser is %s" % ua)
    #return HttpResponse(" Welcome to hello world at %s" % request.path)
    return HttpResponse(" Welcome to hello world"+"\n"+"Search the database for books"+"\n"+"Contact us for any query")

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)	
    return render(request,'current_datetime.html',{'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_metadata(request):
    values1 = request.META.items()
    values1.sort()
    return render(request,'meta.html',{'values_list':values1})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


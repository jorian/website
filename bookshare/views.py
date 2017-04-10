from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime


def index(request):
    return HttpResponse("Hello there!")


def current_datetime(request):
    return render(request, 'current_datetime.html', {'current_date': datetime.datetime.now()})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours, it will be %s." % (offset, dt)
    return HttpResponse(html)

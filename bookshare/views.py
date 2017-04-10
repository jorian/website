from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse("Hello there!")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

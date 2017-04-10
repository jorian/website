from django.http import HttpResponse, Http404
from django.shortcuts import render
from bookshare.models import Book
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


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})

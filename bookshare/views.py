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
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please submit a search term')
        elif len(q) > 20:
            errors.append('Please enter max. 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


def meta_data(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

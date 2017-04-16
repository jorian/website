from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.mail import send_mail

from bookshare.forms import ContactForm
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':form})

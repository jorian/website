from django.shortcuts import render
from website.models import Book


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
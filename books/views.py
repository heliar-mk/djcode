from django.shortcuts import render_to_response
from books.models import Book

def display_meta(request):
        values = request.META.items()
        values.sort()
        return render_to_response('display_meta.html', {'values' :values})


def search(request):
    error = [] 
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Please submit a search term.')
        elif len(q)>20:
            error.append('Please submit a search term less than 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html',{'books':books, 'query':q})
    return render_to_response('search_form.html', {'error':error})

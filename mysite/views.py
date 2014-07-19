from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'offset':offset, 'next_time':next_time})


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

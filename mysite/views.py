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
        path = request.get_full_path()
        is_secure = request.is_secure()
        return render_to_response('display_meta.html', {'values' :values,'path':path, 'is_secure':is_secure})


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.Get['q']:
        q = request.GET['q']
        books = Book.objects.filter(title_icontains=q)
        return render_to_response('search_results.html',{'books':books, 'query':q})
    else:
        return HttpResponse('please submit a search term')

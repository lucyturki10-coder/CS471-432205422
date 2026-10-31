from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    name = request.GET.get('name', 'world!')
    return HttpResponse("Hello, " + name)

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))
def viewbook(request, bookId):
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley',
    }
    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam',
    }

    targetBook = book1 if bookId == 123 else book2
    return render(request, 'bookmodule/show.html', {'book': targetBook})

# Lab 5 - Task 1
def links_view(request):
    return render(request, 'bookmodule/links.html')

# Lab 5 - Task 2
def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')

# Lab 5 - Task 3
def listing_view(request):
    return render(request, 'bookmodule/listing.html')

# Lab 5 - Task 4
def tables_view(request):
    return render(request, 'bookmodule/tables.html')

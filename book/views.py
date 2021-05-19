from django.shortcuts import render
from django.views import generic 

from book.models import book

def index(request):
    return render(request, 'book/book.html')

class BookListView(generic.ListView):
    model = book

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]

    def get_context_data(self, **kwargs):
        
        context = super(BookListView, self).get_context_data(**kwargs)
        
        context['some_data'] = 'This is just some data'
        return context
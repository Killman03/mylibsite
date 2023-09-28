from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Author
from django.views.generic import DetailView

def main(request):
    return render(request, 'library/main.html')

class Book_page(DetailView):
    model = Books
    template_name = 'library/book_page.html'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
# Create your views here.

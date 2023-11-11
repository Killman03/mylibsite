from django.http import HttpResponse

from .models import Books, Rating
from django.views.generic import DetailView, ListView, View
from home.views import menu_name
from .forms import RatingForm

class LibrayHome(ListView):
    model = Books
    template_name = 'library/main.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_name'] = menu_name
        context['title'] = 'Библиотека'
        return context

class Book_page(DetailView):
    model = Books
    template_name = 'library/book_page.html'
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_name'] = menu_name
        context['star_form'] = RatingForm
        return context

class AddStarRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.Meta.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip = self.get_client_ip(request),
                book_id = int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)




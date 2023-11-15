from django.http import HttpResponse, JsonResponse
from django.db.models import Avg
from .models import *
from django.views.generic import DetailView, ListView, View
from home.views import menu_name
from .forms import *
from home.utils import DataMixin
from user.forms import LoginUserForm


class LibrayHome(DataMixin, ListView):
    model = Books
    template_name = 'library/main.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_books'] = Books.objects.all().order_by('id')[:16]
        c_def = self.get_user_context()
        return context | c_def


class Book_page(DataMixin, DetailView):
    model = Books
    template_name = 'library/book_page.html'
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = BookReview.objects.filter(book=self.object)
        context['average_rating'] = BookReview.objects.filter(book=self.object).aggregate(rating=Avg('rating'))
        context['review_form'] = BookReviewForm
        context['last_books'] = Books.objects.all().order_by('id')[:4]
        context['form'] = LoginUserForm
        c_def = self.get_user_context()
        return context | c_def


def ajax_add_review(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Вы забыли зарегестрироваться'}, status=401)

    book = Books.objects.get(pk=pk)
    user = request.user

    review = BookReview.objects.create(
        user=user,
        book=book,
        review=request.POST['review'],
        rating=request.POST['rating']
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating']
    }

    average_rating = BookReview.objects.filter(book=book).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'avg_reviews': average_rating
        }
    )

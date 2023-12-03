from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Avg
from .models import Books
from django.views.generic import DetailView, ListView
from .forms import *
from home.utils import DataMixin
from user.forms import LoginUserForm
from django.shortcuts import render, redirect
from django.contrib import messages


class LibrayHome(DataMixin, ListView):
    model = Books
    template_name = 'library/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Books.objects.all().order_by('-id')[:16]
        context['form'] = SearchForm
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
        context['recommended_books'] = Books.objects.all().order_by('id')[:6]
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


def search_view(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('booksearch')

        if searchedterm == '':
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            results = Books.objects.annotate(search=SearchVector('title', 'description')).filter(search=searchedterm)

            if results:
                context = {'results': results}
                return render(request, 'library/search_book.html', context=context)
            else:
                messages.info(request, 'NO BOOKS')
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))

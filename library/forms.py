from .models import *
from django import forms


class BookReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Отзыв"}))

    class Meta:
        model = BookReview
        fields = ['review', 'rating']

class SearchForm(forms.Form):
    query = forms.CharField()
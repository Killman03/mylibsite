from .models import RatingStar, Rating
from django import forms
class RatingForm(forms.ModelForm):
    CHOICES = [(i, str(i)) for i in range(1, 6)]
    stars = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    # star = forms.ModelChoiceField(
    #     queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    # )
    class Meta:
        model = Rating
        fields = ["star",]


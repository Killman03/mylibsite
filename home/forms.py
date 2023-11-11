from django.forms import ModelForm, TextInput, Textarea
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'your_email', 'subject', 'your_message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Имя & Фамилия'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Тема сообщения'}),
            'your_email': TextInput(attrs={'class': 'input', 'placeholder': 'Адрес почты'}),
            'your_message': Textarea(attrs={'class': 'input', 'placeholder': 'Содержание', 'rows': 5}),
        }
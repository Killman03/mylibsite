from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import ListView, DetailView
from .forms import *
from django.contrib import messages
from .utils import *
from library.models import Books

class Home(DataMixin, ListView):
    template_name = 'home/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['meetings_slider'] = Events.objects.all().order_by('start_time')[:5]
        context['book'] = Books.objects.all().order_by('-id')[:8]
        return context | c_def

    def get_queryset(self):
        # Only display the Setting objects that are active
        return Setting.objects.filter(status=True)

class Meetings(DataMixin, ListView):
    model = Events
    template_name = 'home/meetings.html'
    context_object_name = 'meeting'

    def get_context_data(self, *, object_list=False, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def

def contacts(request):
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() # create relation with model
            data.name = form.cleaned_data['name']
            data.your_email = form.cleaned_data['your_email']
            data.subject = form.cleaned_data['subject']
            data.your_message = form.cleaned_data['your_message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #save data to database
            messages.success(request, 'Uraaa')
            return HttpResponseRedirect('contacts')
    form = ContactForm
    context = {
        'item': Setting.objects.get(pk=1),
        'menu_name': menu_name,
        'form': form
    }
    return render(request, 'home/contacts.html', context=context)

class MeetingDetailView(DataMixin, DetailView):
    model = Events
    template_name = 'home/meeting_details.html'
    slug_url_kwarg = 'meeting_slug'
    context_object_name = 'meeting'
    def get_context_data(self, *, object_list=False, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def


# Create your views here.

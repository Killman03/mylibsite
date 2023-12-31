from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from home.utils import DataMixin
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=False, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def


def logout_user(request):
    logout(request)
    return redirect('login')

# Create your views here.

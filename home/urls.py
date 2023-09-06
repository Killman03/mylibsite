from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("/meetings", meetings, name='meetings'),
    path("/contacts", contacts, name='contacts'),
]


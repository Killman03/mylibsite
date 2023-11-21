from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", cache_page(60)(Home.as_view()), name='home'),
    path("meetings", Meetings.as_view(), name='meetings'),
    path("meeting/<slug:meeting_slug>/", MeetingDetailView.as_view(), name='meeting_details'),
    path("contacts", contacts, name='contacts'),
]


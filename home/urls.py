from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("meetings", Meetings.as_view(), name='meetings'),
    path("about_us", about_us, name='about_us'),
    path("support_project", support_project, name='support_us'),
    path("meeting/<slug:meeting_slug>/", MeetingDetailView.as_view(), name='meeting_details'),
    path("contacts", contacts, name='contacts'),
]


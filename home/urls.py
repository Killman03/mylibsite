from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("meetings", Meetings.as_view(), name='meetings'),
    path("meeting/<slug:meeting_slug>/", MeetingDetailView.as_view(), name='meeting_details'),
    path("contacts", contacts, name='contacts'),
]


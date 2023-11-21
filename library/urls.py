from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", LibrayHome.as_view(), name='library_home'),
    path("<slug:book_slug>/", Book_page.as_view(), name='book_page'),
    path("ajax-add-review/<int:pk>", ajax_add_review, name='ajax_add_review'),
    path("search", search_view, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

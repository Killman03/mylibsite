from django import template
from home.models import Events
from library.models import Books
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('home/show_meeting.html')
def show_meetings():
    all = Events.events_manager.get_queryset().all()
    soon = Events.events_manager.get_queryset().order_by('date')[:3]
    imp = Events.events_manager.get_queryset().filter(is_important=True)
    attr = Events.events_manager.get_queryset().filter(is_attractive=True)
    return {'imp': imp,
            'all': all,
            'soon': soon,
            'attr': attr,
            }

@register.simple_tag()
def get_book_counts():
    return Books.objects.all().count()

@register.simple_tag()
def get_user_counts():
    return User.objects.all().count()
from django import template
from home.models import Events

register = template.Library()

@register.inclusion_tag('home/show_meeting.html')
def show_meetings():
    all = Events.objects.all()
    soon = Events.objects.order_by('date')[:3]
    imp = Events.objects.filter(is_important=True)
    attr = Events.objects.filter(is_attractive=True)
    return {'imp': imp,
            'all': all,
            'soon': soon,
            'attr': attr,
            }
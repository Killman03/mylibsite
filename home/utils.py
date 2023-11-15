from .models import *

menu_name = [
    {'name': 'Главная', 'url_name': 'home'},
    {'name': 'Встречи', 'url_name': 'meetings'},
    {'name': 'Библиотека', 'url_name': 'library_home'},
    {'name': 'Контакты', 'url_name': 'contacts'},
             ]

class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context = kwargs
        setting = Setting.objects.get(pk=1)
        context['item'] = setting
        context['menu_name'] = menu_name
        context.update(kwargs)
        return context
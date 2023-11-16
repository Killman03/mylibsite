from django.utils.deprecation import MiddlewareMixin

class CountVisitsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'visits' in request.session:
            request.session['visits'] += 1
        else:
            request.session['visits'] = 1
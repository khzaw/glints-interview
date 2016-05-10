from django.views.generic.base import TemplateView

class WriteUpTemplateView(TemplateView):
    template_name = 'writeup/index.html'
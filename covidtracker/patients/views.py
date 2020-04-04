from django.http import HttpResponse
import datetime

from django.views.generic import TemplateView


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class HomepageView(TemplateView):
    template_name = "homepage.html"
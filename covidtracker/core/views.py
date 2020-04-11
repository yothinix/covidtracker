from django.views.generic import TemplateView

from patients.models import Patient


class HomeView(TemplateView):
    template_name = "home.html"


class OrderView(TemplateView):
    template_name = "order.html"

    def get(self, request, *args, **kwargs):
        all_patient = Patient.objects.all().order_by('-id')

        context = {
            'all_patient': all_patient
        }

        return self.render_to_response(context)


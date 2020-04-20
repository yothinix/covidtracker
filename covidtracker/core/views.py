from django.views.generic import TemplateView

from patients.models import Patient


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dashboard_menu"] = "active"
        return context


class PatientView(TemplateView):
    template_name = "patient.html"

    def get(self, request, *args, **kwargs):
        all_patient = Patient.objects.all().order_by('-id')

        context = {
            "patient_menu": "active",
            "all_patient": all_patient
        }

        return self.render_to_response(context)


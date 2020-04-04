from django.views.generic import TemplateView


class PatientTemperatureView(TemplateView):
    template_name = "temperature.html"


from django.db import models
from pendulum import timezone

from patients.models import Patient


class TemperatureCheck(models.Model):
    patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    temperature = models.FloatField(null=False, blank=False)
    check_date = models.DateTimeField()
    # check_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.temperature} for {self.patient}"

    @property
    def check_date_in_thai(self):
        thailand = timezone('Asia/Bangkok')
        converted_time = thailand.convert(self.check_date)
        return converted_time

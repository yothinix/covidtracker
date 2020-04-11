from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(max_length=256, null=True, blank=True)
    is_positive = models.BooleanField()
    detail = models.TextField(max_length=1024, null=True, blank=True)
    last_update = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.id}: {self.name} ({self.is_positive})"


from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    image = models.ImageField(upload_to="products")
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ImageField

    def __str__(self):
        return f"{self.id}: {self.name}"

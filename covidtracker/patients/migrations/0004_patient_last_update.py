# Generated by Django 3.0.4 on 2020-04-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='last_update',
            field=models.DateTimeField(null=True),
        ),
    ]

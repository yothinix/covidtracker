# Generated by Django 3.0.4 on 2020-03-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
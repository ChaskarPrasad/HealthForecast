# Generated by Django 4.2.2 on 2023-06-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_diseaseinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaseinfo',
            name='field_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

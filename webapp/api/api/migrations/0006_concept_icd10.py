# Generated by Django 2.2.5 on 2019-09-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_annotatedentity_alternative'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='icd10',
            field=models.TextField(blank=True, default=''),
        ),
    ]

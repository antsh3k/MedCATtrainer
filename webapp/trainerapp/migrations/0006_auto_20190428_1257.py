# Generated by Django 2.2 on 2019-04-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0005_usecase_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usecase',
            name='cntx_size',
        ),
        migrations.AddField(
            model_name='task',
            name='cntx_size',
            field=models.IntegerField(default=7),
        ),
    ]

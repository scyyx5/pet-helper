# Generated by Django 3.2.12 on 2022-03-17 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0066_remove_calender_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='task_d',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_information_remove_reminder_reminder_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='reminder_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-11 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_reminder_user_alter_calender_task_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_note',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_status',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_time',
        ),
    ]

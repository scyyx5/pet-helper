# Generated by Django 3.2.12 on 2022-04-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0081_petowner_reminder_feed_petowner_reminder_walk'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='pet_owner',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='backend.petowner'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-06 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_remove_calender_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.pet'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-12 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_pet_pet_breed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='pet_breed',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='pet_heroid',
        ),
    ]

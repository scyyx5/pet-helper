# Generated by Django 4.0.3 on 2022-03-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_pet_pet_breed_alter_reminder_reminder_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='pet_breed',
        ),
    ]

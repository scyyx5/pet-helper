# Generated by Django 3.2.12 on 2022-03-16 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0055_pet_pet_pic_base64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='pet_pic_base64',
        ),
    ]
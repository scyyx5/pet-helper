# Generated by Django 4.0.3 on 2022-03-13 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0046_information_heroid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='article_image',
        ),
    ]

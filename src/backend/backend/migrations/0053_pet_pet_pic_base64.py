# Generated by Django 3.2.12 on 2022-03-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0052_auto_20220314_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_pic_base64',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
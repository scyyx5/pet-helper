# Generated by Django 4.0.3 on 2022-03-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_alter_pet_pet_heroid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_breed',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_pet_pet_age_alter_pet_pet_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petuser',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
    ]

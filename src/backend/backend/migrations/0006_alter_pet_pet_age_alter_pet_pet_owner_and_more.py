# Generated by Django 4.0.2 on 2022-03-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_pet_alter_petuser_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_age',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_owner',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='petuser',
            name='user_email',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='petuser',
            name='user_phone',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
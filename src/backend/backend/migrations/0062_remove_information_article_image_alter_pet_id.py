# Generated by Django 4.0.3 on 2022-03-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0061_remove_pet_pet_pic_base64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='article_image',
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

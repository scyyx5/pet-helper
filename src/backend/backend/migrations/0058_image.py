# Generated by Django 3.2.12 on 2022-03-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0057_pet_pet_pic_base64'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]

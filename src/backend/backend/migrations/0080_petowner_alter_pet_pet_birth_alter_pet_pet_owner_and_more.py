# Generated by Django 4.0.3 on 2022-04-01 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0079_alter_pet_pet_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fname', models.CharField(default='NA', max_length=100)),
                ('user_lname', models.CharField(default='NA', max_length=100)),
                ('user_email', models.CharField(default='NA', max_length=100)),
                ('user_password', models.CharField(default='NA', max_length=100)),
                ('ally_textSize', models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default='m', max_length=3)),
                ('ally_darkMode', models.CharField(choices=[('1', 'on'), ('0', 'off')], default='0', max_length=1)),
                ('ally_colourBlind', models.CharField(choices=[('None', 'None'), ('Protanopia', 'Protanopia'), ('Protanomaly', 'Protanomaly'), ('Deuteranopia', 'Deuteranopia'), ('Deuteranomaly', 'Deuteranomaly'), ('Tritanopia', 'Tritanopia'), ('Tritanomaly', 'Tritanomaly'), ('Achromatopsia', 'Achromatopsia')], default='None', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_birth',
            field=models.DateField(default=datetime.date(2022, 4, 1)),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_owner',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='backend.petowner'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.petowner'),
        ),
        migrations.DeleteModel(
            name='PetUser',
        ),
    ]

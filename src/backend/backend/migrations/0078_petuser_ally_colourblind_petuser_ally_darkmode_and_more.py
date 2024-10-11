# Generated by Django 4.0.3 on 2022-03-29 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0077_auto_20220325_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='petuser',
            name='ally_colourBlind',
            field=models.CharField(choices=[('none', 'None'), ('protanopia', 'Protanopia'), ('protanomaly', 'Protanomaly'), ('deuteranopia', 'Deuteranopia'), ('deuteranomaly', 'Deuteranomaly'), ('tritanopia', 'Tritanopia'), ('tritanomaly', 'Tritanomaly'), ('achromatopsia', 'Achromatopsia')], default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='petuser',
            name='ally_darkMode',
            field=models.CharField(choices=[('1', 'on'), ('0', 'off')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='petuser',
            name='ally_textSize',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default='m', max_length=3),
        ),
        migrations.AlterField(
            model_name='command',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='information',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_birth',
            field=models.DateField(default=datetime.date(2022, 3, 29)),
        ),
        migrations.AlterField(
            model_name='petuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0104_alter_calendar_id_alter_calendar_ischecked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
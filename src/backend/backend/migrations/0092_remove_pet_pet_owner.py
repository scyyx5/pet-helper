# Generated by Django 4.0.3 on 2022-04-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0091_merge_0082_delete_reminder_0090_auto_20220403_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='pet_owner',
        ),
    ]
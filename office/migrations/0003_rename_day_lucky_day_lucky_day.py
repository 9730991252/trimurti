# Generated by Django 5.1 on 2024-08-27 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_lucky_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lucky_day',
            old_name='day',
            new_name='lucky_day',
        ),
    ]

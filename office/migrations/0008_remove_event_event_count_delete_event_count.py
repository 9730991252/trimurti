# Generated by Django 5.1 on 2024-08-28 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0007_event_count_event_event_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_count',
        ),
        migrations.DeleteModel(
            name='Event_count',
        ),
    ]

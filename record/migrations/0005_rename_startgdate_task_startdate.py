# Generated by Django 4.1.3 on 2024-07-25 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_task_startgdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='startgDate',
            new_name='startDate',
        ),
    ]

# Generated by Django 4.1.3 on 2024-07-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_remove_diagnosis_record_remove_evaluations_record_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='startgDate',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2024-07-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolesToCertify', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='students', to='rolesToCertify.roletocertify'),
        ),
    ]
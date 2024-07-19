# Generated by Django 4.1.3 on 2024-07-19 14:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge', models.TextField()),
                ('isPreferRole', models.BooleanField()),
                ('isPerformedRole', models.BooleanField()),
                ('preferValue', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('performedTime', models.IntegerField()),
                ('rolKnowledge', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal'), ('excellent', 'Excelente')], max_length=9)),
                ('workday', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal')], max_length=9)),
                ('regulation', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal')], max_length=9)),
                ('otherActivities', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal'), ('excellent', 'Excelente')], max_length=9)),
                ('evaluation', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal'), ('excellent', 'Excelente')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='GenericCompetencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('level', models.CharField(choices=[('hight', 'Alto'), ('medium', 'Medio'), ('low', 'Bajo')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposedLvl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('endingDate', models.DateField()),
                ('complexity', models.CharField(choices=[('hight', 'Alto'), ('medium', 'Medio'), ('low', 'Bajo')], max_length=6)),
                ('criticality', models.CharField(choices=[('hight', 'Alto'), ('medium', 'Medio'), ('low', 'Bajo')], max_length=6)),
                ('evaluation', models.CharField(choices=[('good', 'Bien'), ('regular', 'Regular'), ('bad', 'Mal'), ('excellent', 'Excelente')], max_length=9)),
                ('evidence', models.TextField()),
                ('observations', models.TextField()),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='record.record')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificCompetencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('evaluation', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)])),
                ('argumentation', models.TextField()),
                ('lvl', models.CharField(choices=[('not_developed', 'No desarrollada'), ('low_development', 'Bajo desarrollo'), ('medium_development', 'Desarrollo medio'), ('developed', 'Desarrollada')], max_length=18)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_competencies', to='record.record')),
            ],
        ),
    ]

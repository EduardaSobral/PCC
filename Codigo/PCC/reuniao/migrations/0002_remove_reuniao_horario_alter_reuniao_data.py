# Generated by Django 4.1.7 on 2023-04-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reuniao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reuniao',
            name='horario',
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='data',
            field=models.DateTimeField(verbose_name='Data da reunião (00/00/0000   00:00)'),
        ),
    ]

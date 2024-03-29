# Generated by Django 4.1.7 on 2023-04-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reuniao', '0002_remove_reuniao_horario_alter_reuniao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reuniao',
            name='cargos',
            field=models.BooleanField(choices=[(1, 'Cargo 1'), (2, 'Cargo 2'), (3, 'Cargo 3')], default=False),
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='informacoes',
            field=models.CharField(max_length=300, verbose_name='Informações'),
        ),
    ]

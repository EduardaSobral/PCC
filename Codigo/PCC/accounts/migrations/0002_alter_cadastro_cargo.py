# Generated by Django 4.1.7 on 2023-04-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cargo',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
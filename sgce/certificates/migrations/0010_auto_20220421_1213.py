# Generated by Django 2.2.26 on 2022-04-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0009_auto_20220412_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='pos_coordinator',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Cargo Coordenador'),
        ),
        migrations.AddField(
            model_name='template',
            name='pos_manager',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Cargo Diretor'),
        ),
    ]

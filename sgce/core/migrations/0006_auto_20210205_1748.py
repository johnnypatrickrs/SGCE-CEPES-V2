# Generated by Django 2.2.17 on 2021-02-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201116_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='has_public_page',
            field=models.BooleanField(default=False, help_text='\n        Cria uma página pública do evento que mostra todos os certificados.\n        Recomenda-se não marcar essa opção caso o certificado possua dados sensíveis\n        como CPF.\n        ', verbose_name='Criar uma página pública'),
        ),
    ]

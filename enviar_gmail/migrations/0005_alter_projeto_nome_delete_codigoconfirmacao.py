# Generated by Django 5.2 on 2025-04-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviar_gmail', '0004_projeto_codigoconfirmacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='CodigoConfirmacao',
        ),
    ]

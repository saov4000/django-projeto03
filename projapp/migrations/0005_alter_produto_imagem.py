# Generated by Django 5.0.4 on 2024-04-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projapp', '0004_remove_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leitura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='capas_livros/'),
        ),
    ]

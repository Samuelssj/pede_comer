# Generated by Django 3.1.5 on 2021-01-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_endereco_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='nome',
        ),
        migrations.AddField(
            model_name='empresa',
            name='nome',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
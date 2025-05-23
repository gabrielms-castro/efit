# Generated by Django 5.2 on 2025-04-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("treino", "0002_alter_usuario_idade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="nivel_experiencia",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="objetivo",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="peso",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="sexo",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

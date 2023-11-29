# Generated by Django 4.2.7 on 2023-11-29 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Projeto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Relatorio",
            fields=[
                (
                    "idRelatorio",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("descricao", models.TextField(max_length=15000)),
                ("dataRelatorio", models.DateTimeField()),
                (
                    "idProjetoRelatorio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="Projeto.projeto",
                    ),
                ),
            ],
        ),
    ]

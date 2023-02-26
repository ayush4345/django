# Generated by Django 4.1.7 on 2023-02-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(max_length=100)),
                ("emp_code", models.CharField(max_length=5)),
                ("mobile", models.CharField(max_length=10)),
            ],
        ),
    ]

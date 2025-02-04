# Generated by Django 5.1.5 on 2025-01-30 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("department", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("birth_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="CompanyAddress",
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
                ("address", models.TextField()),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="user_api.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hair",
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
                ("color", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hair",
                        to="user_api.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company",
                to="user_api.user",
            ),
        ),
        migrations.CreateModel(
            name="Bank",
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
                ("card_number", models.CharField(max_length=16)),
                ("card_type", models.CharField(max_length=50)),
                ("currency", models.CharField(max_length=50)),
                ("iban", models.CharField(max_length=34)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bank",
                        to="user_api.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAddress",
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
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("post_code", models.IntegerField()),
                ("country", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="user_api.user",
                    ),
                ),
            ],
        ),
    ]

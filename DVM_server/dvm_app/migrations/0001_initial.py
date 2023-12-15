# Generated by Django 4.2.7 on 2023-11-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("rating", models.FloatField()),
            ],
            options={
                "db_table": "orders",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=20)),
                ("stock", models.IntegerField()),
            ],
            options={
                "db_table": "product",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
                ("country", models.CharField(max_length=10)),
                ("welfare", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
    ]

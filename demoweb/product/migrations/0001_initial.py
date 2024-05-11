# Generated by Django 4.2.3 on 2023-07-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="category",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(blank=True, null=True, upload_to="media")),
            ],
        ),
        migrations.CreateModel(
            name="product",
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
                ("title", models.CharField(max_length=100)),
                ("cost", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("discount", models.FloatField()),
                ("image", models.ImageField(upload_to="media")),
                ("is_in_cart", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="product_information",
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
                ("author", models.CharField(max_length=50)),
                ("pages", models.IntegerField()),
                ("publisher", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="informations",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0012_alter_order_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="menthod",
            field=models.IntegerField(
                choices=[(1, "Cash"), (2, "Credit card"), (3, "Bank transfer")],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="note",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Cart"), (2, "Ordered"), (3, "Cancelled")], default=1
            ),
        ),
    ]

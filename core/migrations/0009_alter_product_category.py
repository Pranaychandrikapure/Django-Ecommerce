# Generated by Django 5.0.7 on 2024-07-21 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_product_product_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Category",
                to="core.category",
            ),
        ),
    ]

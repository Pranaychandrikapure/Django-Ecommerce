# Generated by Django 5.0.7 on 2024-07-26 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0015_alter_vendor_cover_image_alter_vendor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimages",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="p_images",
                to="core.product",
            ),
        ),
    ]

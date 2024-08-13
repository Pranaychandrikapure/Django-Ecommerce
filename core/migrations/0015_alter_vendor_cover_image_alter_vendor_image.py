# Generated by Django 5.0.7 on 2024-07-26 11:04

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0014_vendor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="cover_image",
            field=models.ImageField(
                default="vendor.png", upload_to=core.models.user_directory_path
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="image",
            field=models.ImageField(
                default="vendor.png", upload_to=core.models.user_directory_path
            ),
        ),
    ]
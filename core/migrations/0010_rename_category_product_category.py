# Generated by Django 5.0.7 on 2024-07-21 11:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_alter_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Category",
            new_name="category",
        ),
    ]

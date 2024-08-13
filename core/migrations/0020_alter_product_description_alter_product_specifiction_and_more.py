# Generated by Django 5.0.7 on 2024-07-29 19:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0019_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True, default="This is a default description", null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="specifiction",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productreview",
            name="review",
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="address",
            field=ckeditor.fields.RichTextField(
                default="123 Main Street", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True, default="This is a default description", null=True
            ),
        ),
    ]
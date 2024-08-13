# Generated by Django 5.0.7 on 2024-07-20 19:44

import core.models
import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=10,
                        max_length=20,
                        prefix="cat",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Food", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="category/default.png", upload_to="category"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Tags",
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
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("address", models.CharField(max_length=100, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Address",
            },
        ),
        migrations.CreateModel(
            name="CartOrder",
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
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=199, max_digits=9999999.0
                    ),
                ),
                ("paid_status", models.BooleanField(default=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product_status",
                    models.CharField(
                        choices=[
                            ("process", "Processing"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("cancel", "Cancel"),
                        ],
                        default="processing",
                        max_length=30,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Card Order",
            },
        ),
        migrations.CreateModel(
            name="CartOrderItems",
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
                ("invoice_no", models.CharField(max_length=200)),
                ("product_status", models.CharField(max_length=200)),
                ("item", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=199, max_digits=9999999.0
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=199, max_digits=9999999.0
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.cartorder",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cart Order Items",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=10,
                        max_length=20,
                        prefix="pr",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Frsh Pear", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="product/default.png",
                        upload_to=core.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="This is a default description", null=True
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=199, max_digits=9999999.0
                    ),
                ),
                (
                    "old_price",
                    models.DecimalField(
                        decimal_places=2, default=299, max_digits=9999999.0
                    ),
                ),
                ("specifiction", models.TextField(blank=True, null=True)),
                (
                    "product_status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("disabled", "Didsabled"),
                            ("rejected", "Rejected"),
                            ("in_review", "In Review"),
                            ("rejected", "Rejected"),
                        ],
                        default="in_review",
                        max_length=10,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("in_stock", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False)),
                ("digitial", models.BooleanField(default=False)),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=10,
                        max_length=20,
                        prefix="sku",
                        unique=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "Category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.tags",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="ProductImages",
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
                (
                    "image",
                    models.ImageField(
                        default="product.jpg", upload_to="product-images"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products Images",
            },
        ),
        migrations.CreateModel(
            name="ProductReview",
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
                ("review", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "★☆☆☆☆"),
                            (2, "★★☆☆☆"),
                            (3, "★★★☆☆"),
                            (4, "★★★★☆"),
                            (5, "★★★★★"),
                        ],
                        default=1,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Reviews",
            },
        ),
        migrations.CreateModel(
            name="Vendor",
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
                (
                    "vid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=10,
                        max_length=20,
                        prefix="ven",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Netlify", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="vendor/default.png",
                        upload_to=core.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="This is a default description", null=True
                    ),
                ),
                (
                    "address",
                    models.TextField(default="123 Main Street", max_length=100),
                ),
                ("contact", models.CharField(default="000000000000", max_length=100)),
                (
                    "chat_resp_time",
                    models.CharField(default="00:00:00", max_length=100),
                ),
                (
                    "shipping_on_time",
                    models.CharField(default="00:00:00", max_length=100),
                ),
                ("authenticate_rating", models.CharField(default="0", max_length=100)),
                ("days_return", models.CharField(default="0", max_length=100)),
                ("warranty_period", models.CharField(default="0", max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Vendors",
            },
        ),
        migrations.CreateModel(
            name="WishList",
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
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Wish List",
            },
        ),
    ]
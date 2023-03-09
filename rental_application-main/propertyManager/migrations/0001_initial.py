# Generated by Django 4.1.6 on 2023-03-08 13:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="property_to_excel",
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
                ("file", models.FileField(null=True, upload_to="propertyfile")),
            ],
        ),
        migrations.CreateModel(
            name="PropertyDetail",
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
                ("property_name", models.CharField(max_length=200)),
                ("email", models.EmailField(default=None, max_length=254, null=True)),
                ("tenant_name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("bhk", models.IntegerField()),
                ("age", models.IntegerField()),
                ("phone_number", models.CharField(max_length=10)),
                ("rent", models.CharField(max_length=10)),
                ("rent_date", models.DateField(null=True)),
                ("adhar_num", models.CharField(max_length=12)),
                ("adhar_pic", models.FileField(null=True, upload_to="adhar_card")),
                ("rent_due_date", models.IntegerField(default=True)),
                ("is_tenant_active", models.BooleanField(default=True)),
                ("is_paid", models.BooleanField(default=False)),
                ("rent_token", models.CharField(default=uuid.uuid4, max_length=100)),
                (
                    "owner_rent_token_paid",
                    models.CharField(default=uuid.uuid4, max_length=100),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                    "property_pic",
                    models.FileField(null=True, upload_to="Property_image"),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="propertyManager.propertydetail",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 4.1.6 on 2023-03-09 04:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("propertyManager", "0002_propertydetail_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="propertydetail",
            name="owner",
        ),
    ]

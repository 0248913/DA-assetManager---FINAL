# Generated by Django 5.0.3 on 2024-05-29 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AssetManagerApp", "0030_space_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="space",
            old_name="descriptions",
            new_name="description",
        ),
    ]

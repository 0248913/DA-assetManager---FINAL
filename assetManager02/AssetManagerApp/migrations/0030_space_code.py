# Generated by Django 5.0.3 on 2024-05-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "AssetManagerApp",
            "0029_remove_profile_user_remove_spaceroles_space_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="space",
            name="code",
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]

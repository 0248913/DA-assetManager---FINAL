# Generated by Django 5.0.3 on 2024-05-25 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AssetManagerApp", "0019_remove_userlog_in_use_userlog_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userlog",
            name="status",
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-26 10:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AssetManagerApp", "0023_userlog_last_changed_date"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="userlog",
            name="last_changed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="last_changed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

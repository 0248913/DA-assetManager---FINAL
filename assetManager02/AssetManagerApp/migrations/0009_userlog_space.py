# Generated by Django 5.0.3 on 2024-03-26 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagerApp', '0008_remove_userlog_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlog',
            name='space',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AssetManagerApp.space'),
            preserve_default=False,
        ),
    ]

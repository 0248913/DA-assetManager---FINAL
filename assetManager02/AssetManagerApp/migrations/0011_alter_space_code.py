# Generated by Django 5.0.3 on 2024-03-29 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagerApp', '0010_rename_spacemembermanagment_spacemembermanagement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='code',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
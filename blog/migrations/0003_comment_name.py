# Generated by Django 3.2.23 on 2024-01-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20240121_1703"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="name",
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-22 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

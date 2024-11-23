# Generated by Django 4.2.16 on 2024-11-23 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="short_description",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
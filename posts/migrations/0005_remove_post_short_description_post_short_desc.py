# Generated by Django 4.2.16 on 2024-11-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_post_short_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="short_description",
        ),
        migrations.AddField(
            model_name="post",
            name="short_desc",
            field=models.CharField(default="Description", max_length=255),
        ),
    ]
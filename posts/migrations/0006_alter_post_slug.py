# Generated by Django 4.2.16 on 2024-11-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_remove_post_short_description_post_short_desc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

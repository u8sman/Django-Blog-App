# Generated by Django 4.0.3 on 2022-04-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomies', '0006_rename_category_description_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=3, unique=True),
            preserve_default=False,
        ),
    ]

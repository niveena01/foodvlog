# Generated by Django 4.2.2 on 2023-07-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_categ_catego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catego',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categ',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
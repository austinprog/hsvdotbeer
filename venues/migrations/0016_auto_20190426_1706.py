# Generated by Django 2.2 on 2019-04-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0015_populate_venue_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
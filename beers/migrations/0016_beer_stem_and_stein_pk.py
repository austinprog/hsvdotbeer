# Generated by Django 2.1.7 on 2019-02-23 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0015_auto_20190221_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='stem_and_stein_pk',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-26 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_auto_20190425_2158"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="trailer",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]

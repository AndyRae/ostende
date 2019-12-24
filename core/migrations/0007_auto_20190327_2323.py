# Generated by Django 2.1.7 on 2019-03-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_auto_20190324_0136"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="lat",
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="venue",
            name="long",
            field=models.FloatField(blank=True, default=0.0),
            preserve_default=False,
        ),
    ]

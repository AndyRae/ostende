# Generated by Django 2.2.1 on 2019-05-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_auto_20190506_2041"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="quote",
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name="film",
            name="quote_source",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="screening",
            name="audio_description",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="screening",
            name="dementia_friendly",
            field=models.BooleanField(blank=True, default="False"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="screening",
            name="introduction",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="screening",
            name="relaxed_environment",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="screening",
            name="subtitled",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]

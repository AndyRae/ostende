# Generated by Django 2.1.7 on 2019-03-24 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20190324_0022"),
    ]

    operations = [
        migrations.AddField(
            model_name="season",
            name="programme",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Programme",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="articles"),
        ),
        migrations.AlterField(
            model_name="film",
            name="copy",
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="film",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="films"),
        ),
        migrations.AlterField(
            model_name="season",
            name="copy",
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="season",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="seasons"),
        ),
    ]

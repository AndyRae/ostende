# Generated by Django 2.2.1 on 2019-08-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190810_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_credit',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='film',
            name='image_credit',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='season',
            name='image_credit',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='venue',
            name='image_credit',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
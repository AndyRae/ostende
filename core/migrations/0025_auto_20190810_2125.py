# Generated by Django 2.2.1 on 2019-08-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20190810_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_credit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='image_credit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='season',
            name='image_credit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image_credit',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-08 18:40

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_article_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('description', tinymce.models.HTMLField(verbose_name='Text')),
                ('slug', models.SlugField(default='author', editable=False)),
                ('image', models.ImageField(default='default.jpg', help_text='Square dimensions work best', upload_to='authors')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
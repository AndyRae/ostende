# Generated by Django 2.1.7 on 2019-03-23 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_screening_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='./media/default.jpg', upload_to='articles')),
                ('text', models.TextField(max_length=200, null=True)),
                ('slug', models.SlugField(default='article', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('copy', models.TextField(max_length=200, null=True)),
                ('slug', models.SlugField(default='programme', editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.AlterField(
            model_name='screening',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='screening',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='screening',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Season'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='slug',
            field=models.SlugField(default='screening', editable=False),
        ),
        migrations.AlterField(
            model_name='screening',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Venue'),
        ),
        migrations.AddField(
            model_name='article',
            name='programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Programme'),
        ),
        migrations.AddField(
            model_name='screening',
            name='programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Programme'),
        ),
    ]

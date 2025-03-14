# Generated by Django 5.1.6 on 2025-02-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_safaripackage_safariimage_itineraryday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='destination_images/')),
                ('features', models.TextField()),
                ('highlights', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('best_time_to_visit', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]

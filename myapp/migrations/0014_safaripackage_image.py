# Generated by Django 5.1.6 on 2025-03-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_safaripackage_rating_safaripackage_reviews_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='safaripackage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='safari_packages/'),
        ),
    ]

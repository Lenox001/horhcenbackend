# Generated by Django 5.1.6 on 2025-03-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_homepagecontent_extra_paragraph1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='best_time_to_visit',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='features',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='highlights',
        ),
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.CharField(blank=True, help_text='Country where the destination is located.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=5, help_text='Rating out of 5 stars.', null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, help_text='Short description of the destination.', null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='destination_images/'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

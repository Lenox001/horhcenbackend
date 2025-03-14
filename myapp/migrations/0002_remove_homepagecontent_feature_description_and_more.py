# Generated by Django 5.1.6 on 2025-02-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='feature_description',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='hero_image_1',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='hero_image_2',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='title',
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature1_description',
            field=models.TextField(default='Eco-friendly experiences that preserve wildlife and protect the natural beauty of Africa.', help_text='Description for first feature.'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature1_title',
            field=models.CharField(default='Sustainable Safaris', help_text='Title for first feature.', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature2_description',
            field=models.TextField(default='Discover hidden gems and iconic landscapes with experienced guides who know every corner of the wild.', help_text='Description for second feature.'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature2_title',
            field=models.CharField(default='Expert Local Guides', help_text='Title for second feature.', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature3_description',
            field=models.TextField(default='Enjoy the perfect blend of adventure and comfort with our handpicked safari lodges and camps.', help_text='Description for third feature.'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature3_title',
            field=models.CharField(default='Luxury in the Wild', help_text='Title for third feature.', max_length=100),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_background',
            field=models.ImageField(default='features/default.jpg', help_text='Feature section background image.', upload_to='features/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='feature_subtitle',
            field=models.TextField(default='Journey through breathtaking landscapes, encounter majestic wildlife, and immerse yourself in Africa’s wilderness.', help_text='Feature section subtitle.'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hero_image1',
            field=models.ImageField(default='hero/default1.jpg', help_text='First hero image.', upload_to='hero/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hero_image2',
            field=models.ImageField(default='hero/default2.jpg', help_text='Second hero image.', upload_to='hero/'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hero_subtitle',
            field=models.TextField(default='Experience breathtaking landscapes, luxury safari lodges, and unforgettable wildlife adventures.', help_text='Hero section subtitle.'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hero_title',
            field=models.CharField(default='Discover Safari Wonders with Horchen Africa', help_text='Main hero title.', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='feature_title',
            field=models.CharField(default='Experience the Wild Like Never Before', help_text='Main feature section title.', max_length=255),
        ),
    ]

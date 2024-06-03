# Generated by Django 5.0.3 on 2024-04-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_downloadedimage_downloaded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadedimage',
            name='downloaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='downloadedimage',
            name='image_url',
            field=models.URLField(default='/media/images/default-image.jpg'),
        ),
    ]

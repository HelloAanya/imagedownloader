# Generated by Django 5.0.3 on 2024-04-01 10:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_downloadedimage_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadedimage',
            name='url',
        ),
        migrations.AddField(
            model_name='downloadedimage',
            name='downloaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloadedimage',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='downloadedimage',
            name='image_url',
            field=models.URLField(default='https://example.com/default-image-url'),
        ),
    ]

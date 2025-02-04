# Generated by Django 5.0.3 on 2024-04-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_downloadedimage_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadedimage',
            name='url',
        ),
        migrations.AddField(
            model_name='downloadedimage',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='downloadedimage',
            name='downloaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

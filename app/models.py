from django.db import models

class DownloadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    image_url = models.URLField(default='/media/images/default-image.jpg')
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

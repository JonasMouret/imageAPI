from django.db import models

class ImageBelier (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos', max_length=254)

    def __str__(self):
        return self.title


from django.db import models
from django.conf import settings
from PIL import Image
import os
import base64

class ImageBelier (models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='photos', max_length=254, blank=True, null=True)

    HOME = 'HO'
    MAIN = 'MA'
    PARTENAIRES = 'PA'
    CATEGORY_CHOICES = [
        (HOME, 'photo principal'),
        (MAIN, 'photo contenu'),
        (PARTENAIRES, 'partenaires'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=MAIN,
    )
    is_active = models.BooleanField(
        default = True
    )
    image_64 = models.TextField(
        blank = True
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path) 
        if self.category == 'MA':
            output_size = (1100, 1200)
            img.thumbnail(output_size)
        img.save(self.image.path, format="JPEG", quality=70)
        

    def __str__(self):
        return str(self.image)


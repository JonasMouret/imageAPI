from django.db import models
from PIL import Image

class ImageBelier (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos', max_length=254)

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        # area = (150, 200, 800, 800)
        # img.crop(area)
        print(self.category)
        if self.category == 'MA':
            output_size = (1100, 1200)
            img.thumbnail(output_size)
        img.save(self.image.path, format="JPEG", quality=70)

    def __str__(self):
        return self.title


from django.db import models

class ImageBelier (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos', max_length=254)

    CHAMBRES = 'CH'
    PARTENAIRES = 'PA'
    CATEGORY_CHOICES = [
        (CHAMBRES, 'chambres'),
        (PARTENAIRES, 'partenaires'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=CHAMBRES,
    )

    def __str__(self):
        return self.title


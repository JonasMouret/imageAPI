from django.db import models
from django.conf import settings
from PIL import Image
import os
import base64

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
    is_active = models.BooleanField(
        default = True
    )
    image_64 = models.TextField(
        blank = True
        )

    def image_as_base64(self, format='png'):

        if not os.path.isfile(self.image):
            return None
        
        encoded_string = ''
        with open(self.image.path, 'rb') as img_f:
            encoded_string = base64.b64encode(img_f.read())
        return 'data:image/%s;base64,%s' % (format, encoded_string)

    def get_cover_base64(self):
        # settings.MEDIA_ROOT = '/path/to/env/projectname/media'
        return image_as_base64(settings.MEDIA_ROOT + self.cover.path)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # with open(self.image.path, 'rb') as fileImage:
        #     self.image_64 = base64.b64encode(fileImage.read())
        #     self.image_64 = self.image_64.decode('utf8')
        # self.save()
        img = Image.open(self.image.path)
        
        if self.category == 'MA':
            output_size = (1100, 1200)
            img.thumbnail(output_size)
        img.save(self.image.path, format="JPEG", quality=70)
        

    def __str__(self):
        return self.title


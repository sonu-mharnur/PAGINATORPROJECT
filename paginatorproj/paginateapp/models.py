from django.db import models

# Create your models here.
class cities(models.Model):
    city= models.CharField('city',max_length=50)

    def __str__(self):
        return self.city

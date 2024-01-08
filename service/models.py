from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    image = models.ImageField(upload_to = 'service/images/')

    def __str__(self):
        return self.title
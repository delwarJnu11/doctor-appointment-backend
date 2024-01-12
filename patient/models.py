from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='patient/images/')

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
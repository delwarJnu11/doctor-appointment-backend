from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.
class Designation(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 110)

    def __str__(self):
        return self.name
    
class Specialization(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 110)

    def __str__(self):
        return self.name
    
class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    fee = models.IntegerField()
    available_time = models.ManyToManyField(AvailableTime)
    meet_link = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
STARS = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]

class Review(models.Model):
    review = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    body = models.TextField()
    rating = models.CharField(choices = STARS,  max_length = 10)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'Patient: {self.review.user.first_name} || Doctor: {self.doctor.user.first_name}'

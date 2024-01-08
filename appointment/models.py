from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
from appointment.constant import APPOINTMENT_STATUS,APPOINTMENT_TYPE


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment_type = models.CharField(choices = APPOINTMENT_TYPE, max_length = 10)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length = 10, default = 'Pending')
    symptom = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f'Patient: {self.patient.user.first_name} || Doctor: {self.doctor.user.first_name}'
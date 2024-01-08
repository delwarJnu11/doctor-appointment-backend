from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_type', 'appointment_status', 'symptom', 'time', 'cancel']

    def patient_name(self,obj):
        return f'{obj.patient.user.first_name} {obj.patient.user.last_name}'
    
    def doctor_name(self,obj):
        return f'{obj.doctor.user.first_name} {obj.doctor.user.last_name}'
    
admin.site.register(Appointment,AppointmentModelAdmin)
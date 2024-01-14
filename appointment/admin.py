from django.contrib import admin
from .models import Appointment
from patient.views import send_email

# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_type', 'appointment_status', 'symptom', 'time', 'cancel']

    def patient_name(self,obj):
        return f'{obj.patient.user.first_name} {obj.patient.user.last_name}'
    
    def doctor_name(self,obj):
        return f'{obj.doctor.user.first_name} {obj.doctor.user.last_name}'
    
    def save_model(self,request,obj, form,change):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_type == 'Online':
            send_email(obj.patient.user, obj.doctor, 'your appointment is running', 'admin_email.html')
    
admin.site.register(Appointment,AppointmentModelAdmin)
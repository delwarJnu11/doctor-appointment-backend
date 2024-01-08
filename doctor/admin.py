from django.contrib import admin
from doctor.models import Designation,Specialization,AvailableTime,Doctor,Review

# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(AvailableTime)
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from patient.views import PatientViewSet

router = DefaultRouter()
router.register('lists', PatientViewSet)

urlpatterns = [
    path('', include(router.urls))
]

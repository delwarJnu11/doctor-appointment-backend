from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('lists', views.DoctorViewSet)
router.register('specializations', views.SpecializationViewSet)
router.register('designations', views.DesignationViewSet)
router.register('available_times', views.AvailableTimeViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]

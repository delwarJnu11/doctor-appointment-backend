from django.urls import path,include
from rest_framework.routers import DefaultRouter
from patient.views import PatientViewSet,UserRegistrationViewSet,activate,UserLoginViewSet,UserLogoutViewSet

router = DefaultRouter()
router.register('lists', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserRegistrationViewSet.as_view(), name='register' ),
    path('login/',UserLoginViewSet.as_view(), name='login' ),
    path('logout/',UserLogoutViewSet.as_view(), name='logout' ),
    path('activate/<uid64>/<token>/',activate, name='activate' ),
]

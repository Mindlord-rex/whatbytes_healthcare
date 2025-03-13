from django.urls import path
from .views import PatientDoctorMappingViewSet

urlpatterns = [
    path('mappings/', PatientDoctorMappingViewSet.as_view({'get': 'list', 'post': 'create'}), name='mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingViewSet.as_view({'delete': 'destroy'}), name='mapping-detail'),
]
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from vehiculo import views

router = DefaultRouter()
router.register(r'vehicle', views.VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('', include(router.urls)),
    path(r'list_assignmet_vehicle/', views.AssignmentVehiclePerson.as_view({'get':'list'}), name='list_assignment_vehicle'),
    path(r'add_assignmet_vehicle/', views.AssignmentVehiclePerson.as_view({'post':'createAssignmentVehicle'}), name='add_assignment_vehicle'),
]
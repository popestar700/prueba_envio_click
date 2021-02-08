from rest_framework.routers import DefaultRouter
from django.urls import path, include
from persona import views

router = DefaultRouter()
router.register(r'person', views.PersonaViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework import viewsets
from vehiculo.models import Vehicle
from vehiculo.serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def list(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).retrieve(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).destroy(request, args, kwargs)
    
    
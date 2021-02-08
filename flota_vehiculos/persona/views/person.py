from rest_framework import viewsets
from persona.models import Person
from persona.serializers import PersonSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        return super(PersonaViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PersonaViewSet, self).retrieve(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return super(PersonaViewSet,self).create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super(PersonaViewSet, self).update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PersonaViewSet, self).destroy(request, args, kwargs)
    
    
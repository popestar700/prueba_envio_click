from rest_framework import viewsets, status
from rest_framework.response import Response
from vehiculo.models import assignmentVehiclePerson, Vehicle
from persona.models import Person

class AssignmentVehiclePerson(viewsets.ViewSet):
    
    def list(self, resquest, pk=None):
        list_assignment_vehicle = []
        assignment_vehicle_query = assignmentVehiclePerson.objects.all()

        for assignment_vehicle in assignment_vehicle_query:
            list_assignment_vehicle.append(
                {
                    "vehicle": "{0} {1}".format(assignment_vehicle.vehicle.mark, assignment_vehicle.vehicle.model),
                    "person": assignment_vehicle.person.name,
                    "expiration_date": assignment_vehicle.expiration_date
                }
            )
        
        return Response(list_assignment_vehicle, status=status.HTTP_200_OK)

    def createAssignmentVehicle(self, request):
        try:
            data = request.data
            vehicles = Vehicle.objects.filter(person=data['person'])

            for vehicle in vehicles:
                if vehicle.vehicle_assignment:
                    msg = "You already have an assigned car, which is: {0} {1}".format(vehicle.mark , vehicle.model)
                    return Response(msg, status=status.HTTP_401_UNAUTHORIZED)
                    break
            #add new vehicle assignment a person
            vehicle = Vehicle.objects.get(id=data['vehicle'])
            person = Person.objects.get(id=data['person'])
            assignmentVehiclePerson.objects.create(vehicle=vehicle, person=person, expiration_date=data['expiration_date'])

            #Update vehicle_assignment variable
            Vehicle.objects.filter(id=data['vehicle']).update(vehicle_assignment=True)
            msg = "the car was assigned with an expiration date of {0}".format(data['expiration_date'])
            return Response(msg, status=status.HTTP_201_CREATED)
        except:
            raise
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

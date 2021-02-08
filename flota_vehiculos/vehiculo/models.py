from django.db import models
from persona.models import Person
# Create your models here.

class Vehicle(models.Model):
    model = models.CharField(max_length=200, null=True, default="N/A", verbose_name='Model vehicle')
    color = models.CharField(max_length=200, null=False, blank=False, verbose_name='Color vehicle')
    mark = models.CharField(max_length=200, null=False, blank=False, verbose_name='Mark of vehicle')
    vehicle_assignment = models.BooleanField(default=False, verbose_name='vehicle assignment')
    person = models.ForeignKey(Person, related_name='vehicule_person', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True, auto_now=False ,verbose_name='Creation date')
    update_date = models.DateField(auto_now=True, auto_now_add=False ,verbose_name='Update date')

    class Meta:
        db_table = 'vehicle'

class assignmentVehiclePerson(models.Model):
    expiration_date = models.DateField(verbose_name='Expiration date')
    vehicle = models.ForeignKey(Vehicle, related_name='assigment_vehicle', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='assignment_person', on_delete=models.CASCADE)

    class Meta:
        db_table = 'assignment_vehicle_person'
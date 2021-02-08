from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Name of person')
    last_name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Last name')
    email = models.EmailField(max_length=200, null=True, verbose_name='Email contact')
    phone_number = models.BigIntegerField(verbose_name='Number phone contact')
    creation_date = models.DateField(auto_now_add=True, auto_now=False ,verbose_name='Creation date')
    update_date = models.DateField(auto_now=True, auto_now_add=False ,verbose_name='Update date')

    class Meta:
        db_table = 'person'
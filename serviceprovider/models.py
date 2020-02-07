from django.db import models
from djongo.models import EmbeddedModelField, ArrayModelField
from phone_field import PhoneField

# Create your models here.
class Service(models.Model):
    servicename = models.CharField(max_length=120, null=False, blank=False)
    servicedesc = models.CharField(max_length=255, null=False, blank=False)
    servicecost = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

class Appliedservice(models.Model):
    customerid = models.CharField(max_length=10, null=False, blank=False)
    service =  EmbeddedModelField(model_container=Service)
    status = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

class Serviceprovider(models.Model):
    usertype = models.CharField(max_length=10, null=False, blank=False)
    full_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    mobile = PhoneField(null=False, blank=False)
    services = ArrayModelField(model_container=Service)
    appliedservices = ArrayModelField(model_container=Appliedservice)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
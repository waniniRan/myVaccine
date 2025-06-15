from django.db import models
from django.contrib.auth.models import User


# Models that are managed by the system admin are defined here
#The system admin is not defined manually; it will use the in-built superuser that django has

class healthfacility(models.Model):
    name = models.CharField(max_length=200)
    f_ID = models.CharField(max_length=60, unique=True)
    location = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email= models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name}" "({self.f_ID})"
    

class Vaccination(models.Model):
    name= models.CharField(max_length=100)
    v_ID =models.CharField(max_length=50)
    diseasePrevented = models.CharField(max_length=100)
    dose =models.CharField(max_length=50)
    description =models.TextField( blank=True)

    def __str__(self):
        return self.name
    

class facilityadmin(models.Model):
    user =models.OneToOneField (User, on_delete=models.CASCADE)
    facility= models.ForeignKey(healthfacility, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default="Facility Administrator")

    def __str__(self):
       return f"{self.user.get_full_name()} -{self.facility.name}"
         
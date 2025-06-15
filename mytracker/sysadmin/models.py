from django.db import models
from django.contrib.auth.models import User


# Models that are managed by the system admin are defined here
#The system admin is not defined manually; it will use the in-built superuser that django has

class healthfacility(models.Model):
    prefix=models.CharField(max_length=1, unique=True, editable=False) #eg., K , M
    ID = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email= models.EmailField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: #new instances
         self.prefix = self._generate_next_prefix()
         self.ID = f"{self.prefix}0000"
        super().save(*args, **kwargs)   
    
    def _generate_next_prefix(self):
        existing_prefixes = healthfacility.objects.values_list('prefix', flat=True)
        for ascii_code in range(ord('A'), ord('Z') + 1):
            candidate = chr(ascii_code)
            if candidate not in existing_prefixes:
                return candidate
        raise ValueError("All prefixes A-Z are used. Please expand logic.")

    def __str__(self):
        return f"{self.name} ({self.ID})"

class Vaccination(models.Model):
    name= models.CharField(max_length=100)
    v_ID =models.CharField(max_length=50)
    diseasePrevented = models.CharField(max_length=100)
    dose =models.CharField(max_length=50)
    description =models.TextField( blank=True)

    def __str__(self):
        return self.name
    

class Facilityadmin(models.Model):
    user =models.OneToOneField (User, on_delete=models.CASCADE)
    facility= models.ForeignKey(healthfacility, on_delete=models.CASCADE)
    ID= models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.ID:
            prefix = self.facility.prefix
            last_admin = Facilityadmin.objects.filter(
                facility__prefix=prefix,
                ID__startswith=prefix
            ).order_by('-ID').first()

            if last_admin:
                last_number = int(last_admin.ID[1:])
                self.ID = f'{prefix}{last_number + 1:04d}'
            else:
                self.ID = f'{prefix}0001'
        super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.user.username} -{self.facility.name}"
         
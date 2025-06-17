from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import healthfacilityform, Vaccinationform, FacilityAdminCreationForm
from django.contrib.auth.models import User
from .forms import FacilityAdminCreationForm
from .models import healthfacility, Vaccination, Facilityadmin
from django.http import HttpResponse



# define system admin as the super user 
def is_system_admin(user):
  return user.is_superuser

@login_required
@user_passes_test(lambda u: u.is_superuser)
def dashboard (request):
   if request.user.is_superuser:
     return render(request, 'system_admin/dashboard.html' ,{
       'admin_tools': True
     })
   else:
     return render(request, 'no_permission.html')
   
@login_required
@user_passes_test(lambda u: u.is_superuser)
def system_admin_dashboard(request):
     return render(request, 'system_admin/dashboard.html')   
#end


#actions done by the system admninistrator

#REGISTER FACILITY
@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_facility(request):
  if request.method == 'POST':
    form = healthfacilityform(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse("Health facility registered successfully.")
  else:
    form = healthfacilityform()

  if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/register_facility.html', {'form': form})

  return render(request, 'system_admin/dashboard.html', {'form': form})
#LIST FACILITIES
@login_required
@user_passes_test(lambda u: u.is_superuser)
def list_health_facilities(request):
   facilities =healthfacility.objects.all()

   if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/list_health_facilities.html', {'facilities': facilities}) 
   
   return render(request, 'system_admin/dashboard.html',{'facilities': facilities}) 
#end

#CREATE ADMIN
@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_facility_admin(request):
    if request.method == 'POST':
        form = FacilityAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.is_staff = True  # Mark as facility admin
            user.save()

            # Link user to facility
            facility = form.cleaned_data['facility']
            Facilityadmin.objects.create(user=user, facility=facility)

            return HttpResponse ("Facility Admin registered successfully.")
    else:
        form = FacilityAdminCreationForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/create_facility_admin.html', {'form': form})

    return render(request, 'system_admin/dashboard.html', {'form': form})
#LIST ADMINS
login_required
@user_passes_test(lambda u: u.is_superuser)
def list_facility_admins(request):
    admins =Facilityadmin.objects.select_related('user', 'facility')

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/list_facility_admins.html', {'admins': admins})
    
    return render(request, 'system_admin/dashboard.html', {'admins': admins})
#end


#CREATE VACCINES
@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_vaccination(request):
    if request.method == 'POST':
        form = Vaccinationform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Vaccine registered successfully.")
    else:
        form = Vaccinationform()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/create_vaccination.html', {'form': form})

    return render(request, 'system_admin/dashboard.html', {'form': form})
#LIST VACCINES
@login_required
@user_passes_test(lambda u: u.is_superuser)
def list_vaccinations(request):
    vaccinations = Vaccination.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'system_admin/partials/list_vaccinations.html', {'vaccinations': vaccinations})
    
    return render(request, 'system_admin/dashboard.html', {'vaccinations': vaccinations})
#end

    
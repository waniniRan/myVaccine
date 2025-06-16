"""
URL configuration for mytracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import path
from sysadmin import views

urlpatterns = [
    path('',lambda request: redirect('dashboard'),name= 'dashboard'),
    #path('dashboard/',views.system_admin_dashboard, name='dashboard'),
    path('create-facility/', views.register_facility, name='register_facility'),
    path('facilities/', views.list_health_facilities, name='list_facilities'),
    path('create-vaccine/', views.create_vaccination, name='create_vaccine'),
    path('vaccinations/', views.list_vaccinations, name='list_vaccinations'),
    path('create-facility-admin/', views.create_facility_admin, name='create_facility_admin'),
    path('facility-admins/', views.list_facility_admins, name='list_facility_admins'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('admin/', admin.site.urls),

]

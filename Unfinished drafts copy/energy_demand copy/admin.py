from django.contrib import admin

# Register your models here.
from energy_demand.models import EnergyProduction

admin.site.register(EnergyProduction)
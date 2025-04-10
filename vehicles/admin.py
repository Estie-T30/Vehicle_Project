from django.contrib import admin
from .models import Vehicle

# Register your models here.
# admin.site.register(Vehicle)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'vehicle_type', 'color', 'mileage', 'price', 'is_sold', 'created_at', 'updated_at')
    list_filter = ('make', 'model', 'year', 'vehicle_type', 'color')
    search_fields = ('make', 'model', 'vehicle_type')
    ordering = ('-created_at',)

admin.site.register(Vehicle, VehicleAdmin)

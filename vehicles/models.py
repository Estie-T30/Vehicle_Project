from django.db import models

# Create your models here.
VEHICLE_TYPE_CHOICES = (
    ('sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('truck', 'Truck'),
    ('motorcycle', 'Motorcycle')
)

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    color = models.CharField(max_length=50, null=True, blank=True)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


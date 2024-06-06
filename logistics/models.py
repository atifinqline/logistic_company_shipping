from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date


# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.FloatField()
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending')
    shipped_date = models.DateField(db_index=True,default=date(2024, 1, 1))


    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    capacity = models.FloatField()

    def __str__(self):
        return self.vehicle_id

class Shipment(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    origin = models.ForeignKey(Warehouse, related_name='shipment_origin', on_delete=models.CASCADE)
    destination = models.ForeignKey(Warehouse, related_name='shipment_destination', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    shipped_date = models.DateField()
    expected_arrival_date = models.DateField()

    def __str__(self):
        return f"{self.package.name} from {self.origin.name} to {self.destination.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=True)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    
def generate_tracking_number():
    return str(uuid.uuid4())  # This generates a random UUID

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE)  # Ensure Shipment is defined or imported
    order_status = models.CharField(max_length=100)
    placed_at = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=255, unique=True, blank=True)  # Allow blank in Django, will be filled by save method

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = generate_tracking_number()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.tracking_number}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



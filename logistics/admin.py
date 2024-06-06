from django.contrib import admin
from .models import Package, Warehouse, Vehicle, Shipment, Order

admin.site.register(Package)
admin.site.register(Warehouse)
admin.site.register(Vehicle)
admin.site.register(Shipment)
admin.site.register(Order)

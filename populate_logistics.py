import os
import django
from datetime import date
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logistics_project.settings")
django.setup()

from logistics.models import Warehouse, Vehicle, Package, Shipment, Order, Customer
from django.contrib.auth.models import User

def generate_tracking_number():
    return str(uuid.uuid4())

def populate():
    # Assuming a user already exists, otherwise you'll need to create one.
    user1 = User.objects.get(username='existing_user')

    customer1 = Customer(user=user1, company_name="Acme Corp", address="1234 Market St")
    customer1.save()

    warehouse1 = Warehouse(name="West Warehouse", location="5678 West St")
    warehouse1.save()

    vehicle1 = Vehicle(vehicle_id="VH002", type="Van", capacity=500.0)
    vehicle1.save()

    package1 = Package(name="Books", description="Boxes of books", weight=300.0, sender="Publisher", receiver="Library", status="in transit")
    package1.save()

    shipment1 = Shipment(package=package1, origin=warehouse1, destination=warehouse1, vehicle=vehicle1, shipped_date=date.today(), expected_arrival_date=date.today())
    shipment1.save()

    order1 = Order(customer=customer1, shipment=shipment1, order_status="Shipped", placed_at=date.today(), tracking_number=generate_tracking_number())
    order1.save()

if __name__ == '__main__':
    populate()
    print("Data populated successfully.")

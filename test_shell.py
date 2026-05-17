from vehicles.models import Car, Motorcycle

# Clean up existing to avoid duplicates if run multiple times
Car.objects.all().delete()
Motorcycle.objects.all().delete()

# Create 1 Car object
car = Car.objects.create(brand='Toyota', price=500000, doors=4)

# Create 1 Motorcycle object
motorcycle = Motorcycle.objects.create(brand='Honda', price=120000, helmet_included=True)

# Call vehicle_info() on both objects
# Show polymorphism by calling the same method with different outputs
print(">>> car = Car.objects.create(brand='Toyota', price=500000, doors=4)")
print(">>> motorcycle = Motorcycle.objects.create(brand='Honda', price=120000, helmet_included=True)")
print(">>> car.vehicle_info()")
print(car.vehicle_info())
print(">>> motorcycle.vehicle_info()")
print(motorcycle.vehicle_info())

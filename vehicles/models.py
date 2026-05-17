from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        # Format the price to remove trailing decimal zero if it's a whole number
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} costs {formatted_price}"

class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} Car with {self.doors} doors costs {formatted_price}"

class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()

    def vehicle_info(self):
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} Motorcycle costs {formatted_price}"

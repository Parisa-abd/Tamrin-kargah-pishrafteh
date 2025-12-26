class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def show(self):
        print("brand:", self.brand, "| year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    def show(self):
        super().show()
        print("doors:", self.doors)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, sidecar):
        super().__init__(brand, year)
        self.sidecar = sidecar
    def show(self):
        super().show()
        print("sidecar:", self.sidecar)

# objects
cars = [
    Car("Peugeot",2020,4),
    Car("BMW",2022,2),
    Car("Toyota",2019,4),
    Car("Kia",2021,5),
    Car("Mercedes",2023,4)
]

motos = [
    Motorcycle("Honda",2018,"Yes"),
    Motorcycle("Yamaha",2020,"No"),
    Motorcycle("Suzuki",2019,"Yes"),
    Motorcycle("Harley",2021,"No"),
    Motorcycle("Kawasaki",2022,"Yes")
]

vehicles = [
    Vehicle("Generic",2015),
    Vehicle("Ford",2017),
    Vehicle("Mazda",2016),
    Vehicle("Nissan",2018),
    Vehicle("Chevy",2019)
]

print("Cars:")
for c in cars: c.show(); print()

print("Motorcycles:")
for m in motos: m.show(); print()

print("Vehicles:")
for v in vehicles: v.show(); print()

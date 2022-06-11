class Vehicle:
    def _init_(self, brand):
        self.brand = brand
        print(Hi! My name is" + brand)
veh1 = Vehicle("VW")
print(veh1.brand)



class Car:
    brand = 'Volvo'

car1 = Car()
print(car1.brand)

car2 = Car()
print(car2.brand)
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def set_brand(self, my_given_brand):
        self.__brand = my_given_brand
        print("Brand is Updated check it")

    def fullName(self):
        return f"{self.__brand} {self.model}" # formatted string
    
    def fuel_Type(self):
        return "Petrol or Diesel"
    

    @staticmethod
    def general_description():
        return "Cars are means of transport"



class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuel_Type(self):
        return "Electric Charge"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport" 
    

# #####################################################

my_car = Car("Toyota", "Corolla")

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.fullName())


# print(my_car.brand) -> error because it is private
print(my_car.fullName())



my_tesla.set_brand("Tesla_0001")
print(my_tesla.get_brand())



print(Car.general_description())
print(my_tesla.general_description())
""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year
class car(Vehicle): #คลาส car รับถ่ายทอดจากคลาส Vehicle
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
        
    def get_info(self):#overriding method
        return f"brand: {self.brand},Model: {self.model},year:{self.year},number of Doors: {self.number_of_doors}"

mycar = car ("Toyota","Yaris cross",2025,4)
print(mycar.get_info())
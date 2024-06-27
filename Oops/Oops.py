class Car:
    def __init__(self,brand,model):
        self.__brand = brand #-----------------------Private
        self.model = model
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
# -----------------------------------------------------------
    def get_brand(self): #-----------Priavte methods/functions -----
        return self.__brand + '$'  #--------------------------------  Encasulation
        
# ------------------------------------------------------------

    def fuel_type(Self):
        return "Petrol or diesel"
    
    @staticmethod
    def cars_descripotion():
        return "Cars are amazing invention :)"
    
class Electric_Car(Car):
    def __init__(self,brand,model,batter_size):
        
        super().__init__(brand,model)
        
        self.batter_size = batter_size
        
    def fuel_type(Self):
        return "Battery Type"
        
# -----------------------------------------------------------------------
my_Car = Car('Nissan','GTR')
my_elecCar = Electric_Car('Tesla','New','2000')

my_Car.__brand = "Honda"


print(my_Car.__brand)
# print(my_Car.full_name())
# print(my_Car.battery)

# print(my_elecCar.brand,my_elecCar.model,my_elecCar.batter_size)
# print(my_elecCar.get_brand())

# print(my_Car.fuel_type())
# print(my_elecCar.fuel_type())
    
# print(my_Car.cars_descripotion())
# print(Car.cars_descripotion())
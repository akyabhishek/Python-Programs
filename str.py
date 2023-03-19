class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return "a {self.color} car".format(self=self)
        
my_car=Car('red',215)
print(my_car)
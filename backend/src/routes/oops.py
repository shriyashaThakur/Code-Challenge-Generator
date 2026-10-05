class Car:
    number_of_car = 0
    raise_amount= 1.04
    def __init__(self,model,colour,cost):
        self.model = model
        self.colour = colour
        self.cost = cost
        Car.number_of_car += 1
    def info(self):
        return '{} {} {}'.format(self.model, self.colour, self.cost)
    def cost_raise(self):
        self.cost=int(self.cost * self.raise_amount)
    @classmethod
    def new_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_str(cls,str_car):
        model, colour, cost = str_car.split(',')
        return cls(model, colour, cost)


car1 = Car("bmw","pink", 50000)
car2 = Car("honda","white", 60000)
#print(car1.cost)
#car1.cost_raise()
#print(car1.cost)
#print(Car.info(car1))
#(Car.raise_amount)
#print(Car.number_of_car)
car1.raise_amount(20)
print(car1.raise_amount)
print(car2.raise_amount)
car1.new_amount(10)
print(car1.raise_amount)
print(car2.raise_amount)

#str_car1 = 'audi,blue,40000'
#str_car2 = 'wagnor,black,30000'

#new_car1 = Car.from_str(str_car2    )
#print(new_car1.model)



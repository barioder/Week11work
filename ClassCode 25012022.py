# we have a report on the number of flue vaccinations in a class of 40
# it has the following numbers: never : 10 once : 15 twice 7 threetimes : 8
# What is the mean number of the times those people have been vaccinated

noVaccinated = 10
onceVaccinated = 15
twiceVaccinated = 7
thriceVaccinated = 8
classTotal = 40
numVaccinated = onceVaccinated + twiceVaccinated + thriceVaccinated

mean = classTotal/numVaccinated

print(mean)

# create a store class that allow customers purchase items in your store

class store:
    def __init__(self, item, unit_price, item_in_store):

        self.item = item
        self.unit_price = unit_price
        self.items_in_store = item_in_store

    def item_Bought(self, units):
        print(f"You purchased {self.item} at {self.unit_price * units}")

    def items_left(self, units):
        quantity = self.items_in_store - units
        print(f"{quantity} {self.item} left in store ")


z = store("Toy_cars", 500, 25)

z.item_Bought(5)

z.items_left(5)

# create a polymorphism class function

class survive:
    def option1(self):
        print('Take cover')

    def option2(self):
        print('Look out for a safe zone')

    def option3(self):
        print('Run for your life towards safe zones')

class fight:
    def option1(self):
        print('Shield and wait')

    def option2(self):
        print('Look and time for soft sport')

    def option3(self):
        print('Swing Jab with all your might')

surviver = survive()
fighter = fight()

def action(x):
    x.option1()
    x.option2()
    x.option3()

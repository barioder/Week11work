# create a class called 'oddeven' that prints if a number is odd or even in a range of 20

class OddEve:
    def __init__(self, num):
        self.num = num
    def type(self):
        for number in range(self.num):
            if number % 2 == 0:
                print(f'{number} is an even number')
            elif number % 2 == 1:
                print(f'{number} is an odd number')
            else:
                print(f'not sure about {number}')

findout = OddEve(21)
findout.type()
print("------------------------------------------------------")
# 2 create a class that uses a user input to print out your output
class answer:
    def tell(self):
        z = int(input('Input it here  '))
        if z == 0:
            print([i for i in range(1, 10) if i % 2 == 1])

        elif z == 1:
            print([i for i in range(1, 10) if i % 2 == 0])

        else:
            print('That is not valid')


print('Enter 0 for odd')
odd = answer()
odd.tell()

print('Enter 1 for even')
even = answer()
even.tell()
# 3. Create a class that has 3 child classes that inherits from the parent class

class cars:
    def __init__(self, make, color, speedlimit):
        self.make = make
        self.color = color
        self.speedlimt = speedlimit


class bmw(cars):
    def car1Spec(self):
        print(f'This is a {self.make} of color {self.color} with a speed limit of {self.speedlimt}')


class benz(cars):
    def car2Spec(self):
        print(f'This is a {self.make} of color {self.color} with a speed limit of {self.speedlimt}')


class jeep(cars):
    def car3Spec(self):
        print(f'This is a {self.make} of color {self.color} with a speed limit of {self.speedlimt}')


car1 = bmw('BMW', 'Blue', 210)
car2 = benz('Benz', 'Red', 220)
car3 = jeep('Jeep', 'Yellow', 180)

car1.car1Spec()
car2.car2Spec()
car3.car3Spec()

print('---------------------------------------------')
# 4 Create a while loop that is couting down from 10 - 1
z = 10

while True:
    if z < 1:
        break

    print(z)
    z -= 1
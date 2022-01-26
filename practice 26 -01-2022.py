# inheritance

class A:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# inherits from parent class A
class B(A):
    def properties(self):
        print(f'Class B inherits fname {self.fname} and lastname {self.lname} from class A')


c1 = B('Derro', 'Jonah')

c1.properties()


# inheritance with polymophysim

class gym:
    def __init__(self, assign1, assign2, assign3):
        self.assign1 = assign1
        self.assign2 = assign2
        self.assign3 = assign3

class activities(gym):
    def gym_class(self):
        print(f'1st activity is: {self.assign1}')

class activities1(gym):
    def gym_class(self):
        print(f'2nd activity is: {self.assign2}')

class activities2(gym):
    def gym_class(self):
        print(f'3rd activity {self.assign3}')

ac1 = activities('Running', 'Baseball', 'Drills')
ac2 = activities1('jumping', 'Boxing', 'Running')
ac3 = activities2('Resting', 'Soccer', 'Rugby')

ac1.gym_class()
ac2.gym_class()
ac3.gym_class()

class familytree:
    def __init__(self, Dad, Mom, Kid1,Kid2):
        self.Dad = Dad
        self.Mom = Mom
        self.Kid1 = Kid1
        self.kid2 = Kid2

class Brother(familytree):
    def his_hobbie(self, hobbie):
        self.hobbie = hobbie
        print(f'{self.Kid1} enjoys to play videogame {self.hobbie}')


class Sister(familytree):
    def her_hobbie(self):
        print(f'{self.Kid2} enjoys to watch soaps')


class Mother(familytree):
    def mom_hobbie(self):
        print(f'{self.Mom} enjoys to read and write')


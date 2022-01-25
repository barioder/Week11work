# class function
class C:
    m = 24*2
    d = 25//2
    e = 24/2

c3 = C()

print(c3.m)
print(C.d)

class school_subjects:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

s1 = school_subjects("Math", 'Science', 'Reading')

print(s1.sub1)
print(s1.sub2)
print(s1.sub3)

class daysoftheweek:
    def __init__(self, day1, day2, day3, day4):
        self.day1 = day1
        self.day2 = day2
        self.day3 = day3
        self.day4 = day4

days = daysoftheweek('Monday', 'Tue', 'Wed', 'Thurs')

print(days.day1)
print(days.day2)
print(days.day3)
print(days.day4)


class family:
    # thunder method
    def __init__(self, dad, mum, child1, child2):
        self.dad = dad
        self.mum = mum
        self.child1 = child1
        self.child2 = child2

    def family_hobbies(self):
        print("Golfing: " + self.dad)
        print('Reading: ' + self.mum)
        print('Soccer: ' + self.child1)
        print('Music: ' + self.child2)


games = family('Peter', 'Annet', 'Steven', 'Jane')


games.family_hobbies()

import datetime as dt
class bankaccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def walletaccount(self):
        x = dt.datetime.now()
        n = 2567
        print(self.name, self.balance, str(x), str(n))


    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


n1 = bankaccount('Derro', 500)
n2 = bankaccount('Elon', 150)

n1.withdraw(100)

n1.walletaccount()

n1.deposit(10)
n1.walletaccount()

class exercise:
    def first_move(self):
        print('sit ups!')

    def second_move(self):
        print('push ups')

    def third_move(self):
        print('Jogging')

class basketball:
    def first_move(self):
        print('shoot')

    def second_move(self):
        print('PASS')

    def third_move(self):
        print('timeout')

assign1 = exercise()
assign2 = basketball()

def perform(x):
    x.first_move()
    x.second_move()
    x.third_move()

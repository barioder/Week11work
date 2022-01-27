def age():
    ageList = [25, 30, 45, 18, 10]
    n = len(ageList)
    z = 0
    for i in ageList:
        z = z + i

    aveAge = z/n

    return aveAge

print(age())
print('--------------------------------------------------------------')

# 2 .You are given 2D matrix, which represents the number of people in a
# room, group by their eye color and gender. The first row represents
# the male gender,while the second row represents females.
# The colums are the eye colors, in the following order: brown,blue,
# green,black.
# (Create a program that needs to take eye color as input and output the
# percentage of people with the eye color in the room.)

matrix = [['BROWN', 'BLUE', 'GREEN', 'BLACK'], [[5, 15, 4, 3], [4, 10, 2, 5]]]
total = 0
for item in matrix[1]:
    for value in item:
        total = total + value

print('Total number of people in the room is', total)

BrownEyes = matrix[1][0][0] + matrix[1][1][0]
BlueEyes = matrix[1][0][1] + matrix[1][1][1]
GreenEyes = matrix[1][0][2] + matrix[1][1][2]
BlackEyes = matrix[1][0][3] + matrix[1][1][3]
print('Total of Brown eyed people is', BrownEyes)
print('Total of Blue eyed people is', BlueEyes)
print('Total of Green eyed people is', GreenEyes)
print('Total of Black eyed people is', BlackEyes)

while True:
    print(" Enter any of the options below to get their % or 'Q' to Quit: ")
    color = input("'BROWN', 'BLUE', 'GREEN', 'BLACK': ").upper()
    if color == 'BROWN':
        percentage = (BrownEyes / total) * 100
        print(f'The % of Brown Eyes in the room is {percentage}%')
    elif color == 'BLUE':
        percentage = (BlueEyes / total) * 100
        print(f'The % of Blue Eyes in the room is {percentage}%')
    elif color == 'GREEN':
        percentage = (GreenEyes / total) * 100
        print(f'The % of Green Eyes in the room is {percentage}%')
    elif color == 'BLACK':
        percentage = (BlackEyes / total) * 100
        print(f'The % of Green Eyes in the room is {percentage}% ')
    elif color == 'Q':
        print('BYE')
        break

print('--------------------------------------------------------------')
# for

# 3 create a class called bankaccount that has a deposit,withdraw, and statement.
import datetime
class bank:
    def __init__(self, account, balance):
        self.accout = account
        self.balance = balance

    def deposit(self, cashDeposit):
        self.cashDeposit = cashDeposit
        self.balance = self.balance + cashDeposit
        self.dateCD = datetime.datetime.now()
        print(f'Cash deposit of {cashDeposit} on account {self.accout} and your new balance is {self.balance}')

    def withdraw(self, cashWD):
        self.cashWD = cashWD
        self.dateWD = datetime.datetime.now()
        if cashWD < self.balance:
            self.balance = self.balance - cashWD
            print(f'Debit of {cashWD} on account {self.accout} and your new balance is {self.balance}')

    def statement(self):
        print('----------------------------------------------')
        print('your statement as it stands')
        print('----------------------------------------------')
        print('Withdraw of', self.cashWD, 'on', self.dateWD)
        print('Credit of ', self.cashDeposit, 'on', self.dateCD)
        print('------------------------------------------------')
        print('Your Balance is :', self.balance)


acc = bank(2522222, 5000)
acc.deposit(200)
acc.withdraw(150)
acc.statement()

print('--------------------------------------------------------------')
# 4 create a nesting dictionary that prints out all the items in your dictionary


students = {'Derrick': {'Subject': 'Art', 'Class':'S5'},
            'Steven': {'Subject': 'Science', 'Class': 'S6'}}

for key, value in students.items():
    print(key)
    for key2, value2 in value.items():
        print(f'{key2}: {value2}')

    print('********************')



class survive:
    def first_move(self):
        print('sit ups!')

    def second_move(self):
        print('push ups')

    def third_move(self):
        print('Jogging')

class fight:
    def first_move(self):
        print('shoot')

    def second_move(self):
        print('PASS')

    def third_move(self):
        print('timeout')

assign1 = survive()
assign2 = fight()

def perform(x):
    x.first_move()
    x.second_move()
    x.third_move()

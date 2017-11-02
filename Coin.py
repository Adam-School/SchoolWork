import random

# simulate a coin flip
class Coin:
    def __init__(self):
        self.__side_up = 'Heads'



    def toss(self):
        if random.randint(0,1) == 0:
            self.__side_up = 'Heads'
        else:
            self.__side_up = 'Tails'

    def get_side_up(self):
        return self.__side_up

head = 0
tails = 0
temp = 'heads'

for x in range (0 ,50, 1):
    coinflip = Coin()
    temp = coinflip.toss()
    temps = coinflip.get_side_up()
    if temps == 'Heads':
        head += 1
    else:
        tails += 1
print('There was this many heads: ',head,'and there was this many tails: ',tails,' in the 50 coin flips')


# make a office class
class office():

    # a place to hold all vars
    def base(self, category, material, length, width, hight, price):
        self.c = category
        self.m = material
        self.l = length
        self.w = width
        self.h = hight
        self.p = price

    def __str__(self):
        return 'The type of office object is:',self.c,'the material is:',self.m,'the length is:',self.l,'the width is:',self.w,'the hight is:',self.h,'and the price is:',self.p

# a class that extends off of office

class desk(office):
    def setNumD(self, number):
        self.n = number

    def setLocationD(self, location):
        self.lo = location

    def __str__(self):
        return 'The type of office object is:',self.c,'the material is:',self.m,'the length is:',self.l,'the width is:',self.w,'the hight is:',self.h,'and the price is:',self.p,'the amount of draws are:',self.n,'The positions of those draws is:',self.lo

# main to run everything

def main():

    c = input('Please enter a Category')
    m = input('Please enter material')
    l = int(input('Please enter a length'))
    w = int(input('Please enter a width'))
    h = int(input('Please enter a hight'))
    p = int(input('Please enter a price'))

    office1 = office()
    office1.base(c,m,l,w,h,p)
    print(office1.__str__())

    c = input('Please enter a Category')
    m = input('Please enter material')
    l = int(input('Please enter a length'))
    w = int(input('Please enter a width'))
    h = int(input('Please enter a hight'))
    p = int(input('Please enter a price'))
    n = int(input('Please enter how many drawers'))
    x = 0
    while x == 0:
        lo = input('Pleae enter what section they are located (left or right)')
        if lo == 'left':
            x = 1
        elif lo == 'right':
            x = 1
        elif lo == 'Left':
            x = 1
        elif lo == 'Right':
            x = 1

    office2 = desk()
    office2.base(c,m,l,w,h,p)
    office2.setLocationD(lo)
    office2.setNumD(n)
    print(office2.__str__())

# calls main to actually run program

main()




import random
x = 0
v = 0
rint = []
xint = []
yint = []
while x < 20:
    rint.append(random.randint(1,100))
    y = int(input('Enter a number between 1 - 100'))
    while (y < 1 or y > 100):
        print('Please try entering a right number')
        y = int(input('Enter a number between 1 - 100'))
    xint.append(y)
    x += 1
c = max(xint)
m = 0
while m < 20:
    if rint[m] > c:
        yint.append(rint[m])
    m +=1
print('The numbers that were greater than the ones you entered are: ')
while v < len(yint):
    print(yint[v])
    v +=1
if len(yint) == 0:
    print('There was no number that the computer generated greater than the ones you entered')

x = 1
while(x == 1):
    x1 = int(input('Enter a test score 0 - 100'))
    if(x1 <= 100 and x >= 0):
        x = 0
    else:
        print('Enter a number between 1 - 100')
x = 1
while(x == 1):
    x2 = int(input('Enter a test score 0 - 100'))
    if(x2 <= 100 and x >= 0):
        x = 0
    else:
        print('Enter a number between 1 - 100')
x = 1
while(x == 1):
    x3 = int(input('Enter a test score 0 - 100'))
    if(x3 <= 100 and x >= 0):
        x = 0
    else:
        print('Enter a number between 1 - 100')
x = 1
while(x == 1):
    x4 = int(input('Enter a test score 0 - 100'))
    if(x4 <= 100 and x >= 0):
        x = 0
    else:
        print('Enter a number between 1 - 100')
x = 1
while(x == 1):
    x5 = int(input('Enter a test score 0 - 100'))
    if(x5 <= 100 and x >= 0):
        x = 0
    else:
        print('Enter a number between 1 - 100')

def calc_average(x1, x2, x3, x4, x5):
    ave = (x1 + x2 + x3+ x4 + x5)/5
    if(average >= 90):
        print('A')
    elif(average >=80):
        print('B')
    elif(average >= 70):
        print('C')
    elif(average >= 60):
        print('D')
    else:
        print('F')
    return ave
average = calc_average(x1, x2, x3, x4, x5)

print('The average test score is: ', average)

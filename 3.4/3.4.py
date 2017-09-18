print('Package A:	For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.')
print('Package B:	For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.')
print('Package C:	For $69.99 per month unlimited minutes provided')

pack = int(input('Pick your package 1 - 3: '))
min = int(input('How many minutes have you used: '))
if pack == 1:
    if min <= 450:
        print('You spent $39.99 this month')
    else:
        money = (min-450)*.45
        print ('You spent: ','$',format(money, ',.2f'),' This month')
elif pack == 2:
    if min <= 900:
        print('You spent $59.99 this month')
    else:
        money = (min-900)*.40
        print ('You spent: ','$',format(money, ',.2f'),' This month')
elif pack == 2:
    print('You spent $69.99 this month')
else:
    print('No plan selected you dont have any bills to pay')

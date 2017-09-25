money = float(.01)
y = 1
days = int(input('How many days will you work for pennies a day? '))
print ('Days Worked | Amount Earned That Day')
print('------------------------------------')
for x in range (days):
    print(y,'\t',' | ' ,'$',(format(money, ',.2f')))
    money *= 2
    y += 1
print('Total earned over ',days,' days is ','$',(format(money, ',.2f')))

x = 0
average = 0
rain = []
while x < 12:
    y = int(input('How much rainfall was there for this month: '))
    rain.append(y)
    average += y
    x +=1

print('The highest rainfall was: ', max(rain),' which is month number: ',rain.index(max(rain)))
print('The highest rainfall was: ', min(rain),' which is month number: ',rain.index(min(rain)))
print('The average rainfall was: ', average/12)

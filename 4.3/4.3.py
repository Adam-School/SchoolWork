tot = 0
year = int(input('How many years of rain do you want to sit here and read fake news about ? '))
for x in range (year):
    for z in range (12):
        rain = int(input('How much rain fell this month ? '))
        tot += rain
print ('It rained for ', year*12, ' years, total inches of rain fall ',tot,' and the average rainfall monthly is',tot/(year*12),'inches')

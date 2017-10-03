#Adam Emricson
#10/1/2017
#Calorie counter
total = 0
globals()['total'] = 0

# ask for how many grames of fat is eatten and then finds out how many cals that is
def fatCals():
    x = int(input('Enter how many grams of fat did you eat today? '))
    globals()['total'] = total + (x*9)
    print('You ate ',(x*9), 'calories from fat')

# ask for how many grames of carbs is eatten and then finds out how many cals that is
def carbsCals():
    x = int(input('Enter how many grams of carbs did you eat today? '))
    globals()['total'] = total + (x*4)
    print('You ate ',(x*4), 'calories from carbs')

# ask for how many grames of protein is eatten and then finds out how many cals that is
def proteinCals():
    x = int(input('Enter how many grams of protein did you eat today? '))
    globals()['total'] = total + (x*4)
    print('You ate ',(x*4), 'calories from protein')

# prints the global calories
def globCals():
    print('Your total calories for the day were: ',globals()['total'])
fatCals()
carbsCals()
proteinCals()
globCals()


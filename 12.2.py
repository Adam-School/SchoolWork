def main():
    #initialize an variable for the while statement
    x = 1
    y = []
    while x != 0:
        x = int(input('Please enter any number but 0, if you enter a 0 you cant enter anymore numbers'))
        if x != 0:
            y.append(x)
    listPrinter(y, 0)

def listPrinter(x, c):
    #gets the length of the array
    y = int(len(x))
    #the counter
    count = c
    #statement to make sure that it wont keep kalling itself
    if y > 0:
        count += x[y-1]
        del x[-1]
        #call itself
        listPrinter(x,count)
    #gets the final count of the numbers in the array
    if y == 0:
        print(count)
#calls main to run program
main()

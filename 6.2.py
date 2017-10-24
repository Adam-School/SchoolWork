
# make a main function
def main():
    with open("numbers.txt", "r") as ins:
        #create variables to keep track of total and how many numbers were counted
        count = 0
        total = 0
        for line in ins:
            total += int(line)
            count += 1
    print('The average of the numbers in the file.txt is: ', format(total / count, ',.2f') )

# call main function
main()

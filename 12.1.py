def main():
    countDown(int(input('Please enter how high you want to count up to: ')))

# the functiont hat will count down by calling itself
def countDown(count):
    c = count
    if(c > 0):
        countDown(c-1)
        print(c)
main()

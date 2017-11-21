# method to find the power
def expo(num, exp):
    #vars to set the parameters to
    n = num
    e = exp
    # the actual math usuing recusion
    if e == 1:
        return 1
    else:
        e -= 1
        return n*expo(n,e)
# main method
def main():
    x = int(input('enter a number'))
    z = int(input('enter a exponet for that number'))
    print(expo(x, z))

#run program
main()

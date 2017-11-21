
# Making a class

class Employee():

    def setNumber(self, num):
        self.number = num

    def setName(self, name):
        self.name = name

    def getName(self):
        return 'Employee Name '+ self.name

    def getNumber(self):
        return 'Employee Number',self.number

# making a class append off of Employee

class ProductionWorker(Employee):

    def setHourlyPay(self, pay):
        self.hpay = 'you make',pay,'hourly'

    def setShiftNum(self, snum):
        self.shift ='you work the:',snum

    def getShiftNum(self):
        if self.shift == 1:
            return 'Day Shift'
        elif self.shift == 2:
            return 'Night Shift'
        else:
            return 'You are working on an imaginary shift'

    def getHourlyPay(self):
        return self.hpay


def main():
    # set a variable for the while loop
    x = 0


    #print out an Employee class
    Employee1 = Employee()
    Employee1.setNumber(int(input('Please enter an Employee number: ')))
    Employee1.setName(input('Please enter your Employee name: '))
    print(Employee1.getName())
    print(Employee1.getNumber())

    #actually make a object that appends off Employee
    Employee2 = ProductionWorker()
    Employee2.setNumber(int(input('Please enter an Employee number: ')))
    Employee2.setName(input('Please enter your Employee name: '))

    # Check whether or not they enter a correct shift
    while x == 0:
        y = int(input('Please enter what shift you are working (1 - day)(2 - night): '))
        if y == 1:
            Employee2.setShiftNum(y)
            x = 1
        elif y == 2:
            Employee2.setShiftNum(y)
            x = 1

    Employee2.setHourlyPay(int(input('Please enter your hourly pay rate: ')))
    print(Employee2.getName())
    print(Employee2.getNumber())
    print(Employee2.getShiftNum())
    print(Employee2.getHourlyPay())

# Run the program
main()

class info:
    #setting the name for the person
    def setName(self, names):
        self.name = names

    #setting the address for the person
    def setAddress(self, add):
        self.address = add

    #setting the age of the person
    def setAge(self, ages):
        self.age = ages

    #setting the phone number of the person
    def setPhone(self, number):
        self.phone = number

    #getting the name
    def getName(self):
        return self.name

    #getting the address
    def getAddress(self):
        return self.address

    #getting the age
    def getAge(self):
        return self.age

    #getting the phone number
    def getPhone(self):
        return self.phone

def main():

    #this section of code is for the user to input their own info
    name = input('Please enter your name: ')
    address = input('Please enter your address: ')
    age = int(input('Please enter your Age: '))
    phone = input('Please enter your phone number')

    person1 = info()
    person1.setName(name)
    person1.setAddress(address)
    person1.setAge(age)
    person1.setPhone(phone)

    print('Person 1\'s name: ',person1.getName())
    print('Person 1\'s address: ',person1.getAddress())
    print('Person 1\'s age: ',person1.getAge())
    print('Person 1\'s phone number: ',person1.getPhone())

    print('--------------------------------------------------------------------------')

    #Person 2 made by me
    person2 = info()
    person2.setName('Joe')
    person2.setAddress('435 Kings court')
    person2.setAge(23)
    person2.setPhone('000-000-0001')

    print('Person 2\'s name: ',person2.getName())
    print('Person 2\'s address: ',person2.getAddress())
    print('Person 2\'s age: ',person2.getAge())
    print('Person 2\'s phone number: ',person2.getPhone())

    print('--------------------------------------------------------------------------')

    #person 3 also made by me
    person3 = info()
    person3.setName('David E')
    person3.setAddress('none')
    person3.setAge('Unknown')
    person3.setPhone('~Error~')

    print('Person 3\'s name: ',person3.getName())
    print('Person 3\'s address: ',person3.getAddress())
    print('Person 3\'s age: ',person3.getAge())
    print('Person 3\'s phone number: ',person3.getPhone())

#calls main to actually run the program
main()

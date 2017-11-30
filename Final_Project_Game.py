import time
import random

# create a class for the player.
class Player:
    # the initializer
    def __init__(self):
        # name for the character
        self.name=''
        # health of the character
        self.health = 20
        # max health for the character
        self.max_health = 20
        # str of character
        self.strength = 1
        # armor class of character
        self.AC = 1
        # dex of the characeter
        self.dexterity = 1
        # intelegence of the character
        self.intellegence = 1
        # gold of the character
        self.gold = 0
        # player inventory
        self.inventory = []

    # set the name of the character
    def setName(self, Name):
        self.name = Name

    # get the name of the character
    def getName(self):
        return self.name

    # set the health of the character
    def setHealth(self, hp):
        self.health = hp

    # get the health of the character
    def getHealth(self):
        return self.health

    # set the max health of character
    def setMaxHealth(self, hp):
        self.max_health = hp

    # get the max health of the character
    def getMaxHealth(self):
        return self.max_health

    # set the str of the character
    def setStr(self, str):
        self.strength = str

    # get the str of the character
    def getStr(self):
        return self.strength

    # set the armor class of the character
    def setAC(self, ac):
        self.AC = ac

    # get the armor class of the character
    def getAC(self):
        return self.AC

    # set the dex of the character
    def setDex(self, dex):
        self.dexterity = dex

    # get the dex of the character
    def getDex(self):
        return self.dexterity

    # set the Int of the character
    def setInt(self, int):
        self.intellegence = int

    # get the Int of the character
    def getInt(self):
        return self.intellegence

    # add to gold of the character
    def addGold(self, added):
        self.gold += added

    # subtract gold of the character
    def subGold(self, sub):
        self.gold -= sub

    # get the gold of the character
    def getGold(self):
        return self.gold

    # add to the Inventory of the character
    def addInv(self, item):
        self.inventory.append(item)

    # remove item from Inventory of the character
    def removeInv(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
             pass

    # get the inventory of the character
    def getInventory(self):
        return self.inventory

    # get a item from inventory of character
    def getItem(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    # print the stats of the character
    def printChar(self):
        print('======================================================')
        print('Your Character Name is: ',self.name)
        print('Your Character\'s Max Health is: ',self.max_health)
        print('Your Character\'s Current Health is: ',self.health)
        print('Your stats are: ','Str: ',self.strength,' Dex: ',self.dexterity,' Int: ',self.intellegence)
        print('Your armor class is: ',self.AC)
        print('Your gold is: ',self.gold)
        print('======================================================')

# class to make a AI
class AI:
    # the initializer
    def __init__(self):
        # name for the mob
        self.name=''
        # health of the mob
        self.health=5
        # max health of the mob
        self.max_health = 5
        # str of mob
        self.strength = 1
        # armor class of mob
        self.AC = 1
        # dex of the mob
        self.dexterity = 1
        # int of the mob
        self.intellegence = 1
        # loot of the mob
        self.loot = []


    # set the name for the mob
    def setName(self, Name):
        self.name = Name

    # get the name of the mob
    def getName(self):
        return self.name

    # set the Maxhealth
    def setMaxHealth(self, hp):
        self.max_health = hp

    # get the Maxhealth of the mob
    def getMaxHealth(self):
        return self.max_health

    # set the health of mob
    def setHealth(self, hp):
        self.health = hp

    # get the current health of the mob
    def getHealth(self):
        return self.health

    # set the Str of a mob
    def setStr(self, str):
        self.strength = str

    # get the Str of the mob
    def getStr(self):
        return self.strength

    # set the armor class of the mob
    def setAC(self, ac):
        self.AC = ac

    # get the armor class of the mob
    def getAC(self):
        return self.AC

    # set the dex of the mob
    def setDex(self, dex):
        self.dexterity = dex

    # get the dex of the mob
    def getDex(self):
        return self.dexterity

    # set the intellegence of the mob
    def setInt(self, int):
        self.intellegence = int

    # get the Int of the mob
    def getInt(self):
        return self.intellegence

    # set the loot of the mob
    def addLoot(self, stuff):
        self.loot = stuff

    # get the loot of the mob
    def getLoot(self):
        return self.loot

# the main function of the game
def main():
    tempInput = 5
    i = 0
    rolls = []
    finalRoll = []
    print('This is a game created by Adam Emricson\nLast time this was edited was Wednesday 29th 2017\nAnd this game will be a text based DnD style game')
    time.sleep(5)
    cls()
    player = Player()
    player.setName(input('Please enter your characters name (what you want to be refrenced by)'))
    # a while statement to get 3 rolls for your int, str, dex
    while i < 9:
        rolls.append(random.randint(0,20))
        if i == 2:
            finalRoll.append(max(rolls))
            del rolls[:]
        elif i == 5:
            finalRoll.append(max(rolls))
            del rolls [:]
        elif i == 8:
            finalRoll.append(max(rolls))
            del rolls [:]
        i += 1
    print('The computer will roll 9 d20\'s and take the top 3 rolls for your stats')
    print(finalRoll)
    while tempInput != 0 or tempInput != 1 or tempInput != 2:
        if tempInput == 5:
            tempInput = int(input('To select the rolls they go from 0, 1, 2 (choose 0 for the first stat choose 1 for second stat)\nNow choose the stat you want for Strength'))
        else:
            tempInput = int(input('You entered an invalid number please enter 0, 1, 2'))

    tempInput = 5
    player.setStr(finalRoll[tempInput])
    finalRoll.remove(finalRoll[tempInput])

    print(finalRoll)
    while tempInput != 0 or tempInput != 1:
        if tempInput == 5:
            tempInput = int(input('To select the rolls they go from 0, 1 (choose 0 for the first stat choose 1 for second stat)\nNow choose the stat you want for Dexterity'))
        else:
            tempInput = int(input('You entered an invalid number please enter 0, 1'))

    player.setDex(finalRoll[tempInput])
    finalRoll.remove(finalRoll[tempInput])

    print('And your final stat for Intellegence is: ',finalRoll[0])

    player.setInt(finalRoll[0])
    del finalRoll[:]

    cls()
    player.printChar()


# clear the screen or so to say
def cls(): print ("\n" * 50)


main()


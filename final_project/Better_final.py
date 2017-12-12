import time
import random
import pprint
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# create a class for the player.
class Player:
    # the initializer
    def __init__(self):
        # Name for the character
        self.name=''
        # Health of the character
        self.health = 20
        # Max health for the character
        self.max_health = 20
        # Str of character
        self.strength = 1
        # Armor class of character
        self.AC = 1
        # Dex of the characeter
        self.dexterity = 1
        # Intelegence of the character
        self.intellegence = 1
        # Gold of the character
        self.gold = 0
        # Character inventory
        self.inventory = []
        # Character race
        self.race = ''
        # Character color if dragonborn
        self.color = 'Not a dragonborn'
        # Character's racial ability
        self.raceAbility = []
        # Character's racial ability description
        self.raceAbilityDisc = []
        # Character Class
        self.charClass = ''
        # Character's saving throws
        self.savingThrow = []
        # Character Level
        self.charLevel = 1
        # Character Proficiency
        self.proficiency = 0
        # Character's Rage for Barbarian
        self.rage = 0
        # Character's Rage damage
        self.rageDmg = 0
        # Characters Features
        self.features = []
        # Character Proficiencies
        self.proficiencies = []
        # Character Skills
        self.skills = []
        # Character Equipment
        self.equipment = []
        # Character Hp dice at higher level
        self.hpDice = 0
        # Character subClass
        self.path = ''
        # Character subClass features
        self.pathFeatures = []
        # Character Charisma
        self.charisma = 0
        # Character Wisdom
        self.wisdom = 0
        # Character Constitution
        self.constitution = 0
        # Character Strength mod
        self.strengthMod = 0
        # Character Dexterity mod
        self.dexterityMod = 0
        # Character Constitution mod
        self.constitutionMod = 0
        # Character Itellegence mod
        self.intellegenceMod = 0
        # Character Wisdom mod
        self.wisdomMod = 0
        # Character Charisma mod
        self.charismaMod = 0
        # Character Cantrip slots
        self.cantripSlots = []
        # Character spell slots
        self.spellSlots = []
        # Characters max cantrip slots
        self.maxCantripSlots = 0
        # Characters max spell slots
        self.maxSpellSlots = 0
        # Characters max first spells
        self.firstSpellMax = 0
        # Characters max second spells
        self.secondSpellMax = 0
        # Characters max thrid spells
        self.thirdSpellMax = 0
        # Characters max fourth spells
        self.fourthSpellMax = 0
        # Characters max fifth spells
        self.fifthSpellMax = 0
        # Characters max sixth spells
        self.sixthSpellMax = 0
        # Characters max seventh spells
        self.seventhSpellMAx = 0
        # Characters max eighth spells
        self.eighthSpellMax = 0
        # Characters max ninth spells
        self.ninthSpellMax = 0
        # Characters weapon
        self.weapon = ''
        # Characters weapon dmg
        self.dmg = 0
        # Characters weapon dice
        self.dmgDice = 0
        # Weapon list
        self.weaponList = ['Battleaxe', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer', 'Whip']
        # armor
        self.armor = 0

    # set the name of the character
    def setName(self, Name):
        self.name = Name

    # set the constitution of the character
    def setConstitution(self, const):
        self.constitution = const

    # get the constitution of the character
    def getConstitution(self):
        return self.constitution

    # set Wisdom of the character
    def setWidsom(self, wis):
        self.wisdom = wis

    # set Charisma of the character
    def setCharisma(self, cha):
        self.charisma = cha

    # set the Strength mod
    def setStrengthMod(self, str):
        if str == 1:
            self.strengthMod = -5
        elif str >= 2 and str <= 3:
            self.strengthMod = -4
        elif str >= 4 and str <= 5:
            self.strengthMod = -3
        elif str >= 6 and str <= 7:
            self.strengthMod = -2
        elif str >= 8 and str <= 9:
            self.strengthMod = -1
        elif str >= 10 and str <= 11:
            self.strengthMod = 0
        elif str >= 12 and str <= 13:
            self.strengthMod = 1
        elif str >= 14 and str <= 15:
            self.strengthMod = 2
        elif str >= 16 and str <= 17:
            self.strengthMod = 3
        elif str >= 18 and str <= 19:
            self.strengthMod = 4
        elif str >= 20 and str <= 21:
            self.strengthMod = 5
        elif str >= 22 and str <= 23:
            self.strengthMod = 6
        elif str >= 24 and str <= 25:
            self.strengthMod = 7
        elif str >= 26 and str <= 27:
            self.strengthMod = 8
        elif str >= 28 and str <= 29:
            self.strengthMod = 9
        elif str == 30:
            self.strengthMod = 10

    # set the Dexterity mod
    def setDexterityMod(self, str):
        if str == 1:
            self.dexterityMod = -5
        elif str >= 2 and str <= 3:
            self.dexterityMod = -4
        elif str >= 4 and str <= 5:
            self.dexterityMod = -3
        elif str >= 6 and str <= 7:
            self.dexterityMod = -2
        elif str >= 8 and str <= 9:
            self.dexterityMod = -1
        elif str >= 10 and str <= 11:
            self.dexterityMod = 0
        elif str >= 12 and str <= 13:
            self.dexterityMod = 1
        elif str >= 14 and str <= 15:
            self.dexterityMod = 2
        elif str >= 16 and str <= 17:
            self.dexterityMod = 3
        elif str >= 18 and str <= 19:
            self.dexterityMod = 4
        elif str >= 20 and str <= 21:
            self.dexterityMod = 5
        elif str >= 22 and str <= 23:
            self.dexterityMod = 6
        elif str >= 24 and str <= 25:
            self.dexterityMod = 7
        elif str >= 26 and str <= 27:
            self.dexterityMod = 8
        elif str >= 28 and str <= 29:
            self.dexterityMod = 9
        elif str == 30:
            self.dexterityMod = 10

    # set the Constitution mod
    def setConstitutionMod(self, str):
        if str == 1:
            self.constitutionMod = -5
        elif str >= 2 and str <= 3:
            self.constitutionMod = -4
        elif str >= 4 and str <= 5:
            self.constitutionMod = -3
        elif str >= 6 and str <= 7:
            self.constitutionMod = -2
        elif str >= 8 and str <= 9:
            self.constitutionMod = -1
        elif str >= 10 and str <= 11:
            self.constitutionMod = 0
        elif str >= 12 and str <= 13:
            self.constitutionMod = 1
        elif str >= 14 and str <= 15:
            self.constitutionMod = 2
        elif str >= 16 and str <= 17:
            self.constitutionMod = 3
        elif str >= 18 and str <= 19:
            self.constitutionMod = 4
        elif str >= 20 and str <= 21:
            self.constitutionMod = 5
        elif str >= 22 and str <= 23:
            self.constitutionMod = 6
        elif str >= 24 and str <= 25:
            self.constitutionMod = 7
        elif str >= 26 and str <= 27:
            self.constitutionMod = 8
        elif str >= 28 and str <= 29:
            self.constitutionMod = 9
        elif str == 30:
            self.constitutionMod = 10

    # set the Intellegence mod
    def setIntellegenceMod(self, str):
        if str == 1:
            self.intellegenceMod = -5
        elif str >= 2 and str <= 3:
            self.intellegenceMod = -4
        elif str >= 4 and str <= 5:
            self.intellegenceMod = -3
        elif str >= 6 and str <= 7:
            self.intellegenceMod = -2
        elif str >= 8 and str <= 9:
            self.intellegenceMod = -1
        elif str >= 10 and str <= 11:
            self.intellegenceMod = 0
        elif str >= 12 and str <= 13:
            self.intellegenceMod = 1
        elif str >= 14 and str <= 15:
            self.intellegenceMod = 2
        elif str >= 16 and str <= 17:
            self.intellegenceMod = 3
        elif str >= 18 and str <= 19:
            self.intellegenceMod = 4
        elif str >= 20 and str <= 21:
            self.intellegenceMod = 5
        elif str >= 22 and str <= 23:
            self.intellegenceMod = 6
        elif str >= 24 and str <= 25:
            self.intellegenceMod = 7
        elif str >= 26 and str <= 27:
            self.intellegenceMod = 8
        elif str >= 28 and str <= 29:
            self.intellegenceMod = 9
        elif str == 30:
            self.intellegenceMod = 10

    # set the Wisdom mod
    def setWisdomMod(self, str):
        if str == 1:
            self.wisdomMod = -5
        elif str >= 2 and str <= 3:
            self.wisdomMod = -4
        elif str >= 4 and str <= 5:
            self.wisdomMod = -3
        elif str >= 6 and str <= 7:
            self.wisdomMod = -2
        elif str >= 8 and str <= 9:
            self.wisdomMod = -1
        elif str >= 10 and str <= 11:
            self.wisdomMod = 0
        elif str >= 12 and str <= 13:
            self.wisdomMod = 1
        elif str >= 14 and str <= 15:
            self.wisdomMod = 2
        elif str >= 16 and str <= 17:
            self.wisdomMod = 3
        elif str >= 18 and str <= 19:
            self.wisdomMod = 4
        elif str >= 20 and str <= 21:
            self.wisdomMod = 5
        elif str >= 22 and str <= 23:
            self.wisdomMod = 6
        elif str >= 24 and str <= 25:
            self.wisdomMod = 7
        elif str >= 26 and str <= 27:
            self.wisdomMod = 8
        elif str >= 28 and str <= 29:
            self.wisdomMod = 9
        elif str == 30:
            self.wisdomMod = 10

    # set the Charisma mod
    def setCharismaMod(self, str):
        if str == 1:
            self.charismaMod = -5
        elif str >= 2 and str <= 3:
            self.charismaMod = -4
        elif str >= 4 and str <= 5:
            self.charismaMod = -3
        elif str >= 6 and str <= 7:
            self.charismaMod = -2
        elif str >= 8 and str <= 9:
            self.charismaMod = -1
        elif str >= 10 and str <= 11:
            self.charismaMod = 0
        elif str >= 12 and str <= 13:
            self.charismaMod = 1
        elif str >= 14 and str <= 15:
            self.charismaMod = 2
        elif str >= 16 and str <= 17:
            self.charismaMod = 3
        elif str >= 18 and str <= 19:
            self.charismaMod = 4
        elif str >= 20 and str <= 21:
            self.charismaMod = 5
        elif str >= 22 and str <= 23:
            self.charismaMod = 6
        elif str >= 24 and str <= 25:
            self.charismaMod = 7
        elif str >= 26 and str <= 27:
            self.charismaMod = 8
        elif str >= 28 and str <= 29:
            self.charismaMod = 9
        elif str == 30:
            self.charismaMod = 10

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

    # set the color of the characters dragon born
    def setColor(self, Color):
        self.color = Color

    # get the color of the character's dragonborn
    def getColor(self):
        return self.color

    # print the stats of the character
    def printChar(self):
        print('======================================================')
        print('Your Character Name is: ',self.name)
        print('Your Characters Race is: ',self.race)
        print('Your Character\'s Class is: ',self.charClass)
        print('Your Character\'s Level is: ',self.charLevel)
        print('Your Hp Dice are: ',self.hpDice)
        print('Your Character\'s Max Health is: ',self.max_health)
        print('Your Character\'s Current Health is: ',self.health)
        print('Your stats are: ','Str: ',self.strength,' Dex: ',self.dexterity,' Int: ',self.intellegence)
        print('Your other stats are: ','Cont: ', self.constitution,' Char: ',self.charisma,' Wis: ',self.wisdom)
        print('Your armor class is: ',self.AC)
        print('Your gold is: ',self.gold)
        print('======================================================')

    # set character race
    def setRace(self, Race):
        self.race = Race.lower()
        if self.race.lower() == 'dragonborn' or self.race.lower == 'dragon born':
            print('please enter the color of your ', self.race)
            print('Damage Type	Breath Weapon')
            print('==========================================================')
            print('Black	Acid        Breath	5 by 30 ft. line (Dex. save)')
            print('Blue     Lightning   Breath	5 by 30 ft. line (Dex. save)')
            print('Brass	Fire	    Breath  5 by 30 ft. line (Dex. save)')
            print('Bronze	Lightning	Breath  5 by 30 ft. line (Dex. save)')
            print('Copper	Acid	    Breath  5 by 30 ft. line (Dex. save)')
            print('Gold	    Fire	    Breath  15 ft. cone (Dex. save)')
            print('Green	Poison	    Breath  15 ft. cone (Con. save)')
            print('Red	    Fire	    Breath  15 ft. cone (Dex. save)')
            print('Silver	Cold	    Breath  15 ft. cone (Con. save)')
            print('White	Cold	    Breath  15 ft. cone (Con. save)')
            print('==========================================================')
            print('What color is your dragonborn?')
            x = 0
            tempInput = ''
            while x == 0:
                if self.race.lower() == 'dragonborn' or self.race.lower() == 'dragon born':
                    tempInput = input().lower()
                    if tempInput == 'black':
                        x = 1
                    elif tempInput == 'blue':
                        x = 1
                    elif tempInput == 'brass':
                        x = 1
                    elif tempInput == 'bronze':
                        x = 1
                    elif tempInput == 'copper':
                        x = 1
                    elif tempInput == 'gold':
                        x = 1
                    elif tempInput == 'green':
                        x = 1
                    elif tempInput == 'red':
                        x = 1
                    elif tempInput == 'silver':
                        x = 1
                    elif tempInput == 'white':
                        x = 1
                    else:
                        print('Invalid color')
            self.setColor(tempInput)

    # get character's race
    def getRace(self):
        return self.race

    # set race ability
    def setRaceAbility(self):
        # deletes everything in raceAbility and raceAbilityDisc
        del self.raceAbility[:]
        del self.raceAbilityDisc[:]
        if self.race == 'dragonborn' or self.race == 'dragon born':
            if self.color == 'black':
                self.raceAbility.append('Acid Breath')
                self.raceAbility.append('Damage Resistance: Acid')
                self.raceAbilityDisc.append('Acid Breath 5 by 30 ft. line')
            elif self.color == 'blue':
                self.raceAbility.append('Lightning Breath')
                self.raceAbility.append('Damage Resistance: Lightning')
                self.raceAbilityDisc.append('Lightning Breath 5 by 30 ft. line')
            elif self.color == 'brass':
                self.raceAbility.append('Fire Breath')
                self.raceAbility.append('Damage Resistance: Fire')
                self.raceAbilityDisc.append('Fire Breath 5 by 30 ft line')
            elif self.color == 'bronze':
                self.raceAbility.append('Lightning Breath')
                self.raceAbility.append('Damage Resistance: Lightning')
                self.raceAbilityDisc.append('Lightning Breath 5 by 30 ft. line')
            elif self.color == 'copper':
                self.raceAbility.append('Acid Breath')
                self.raceAbility.append('Damage Resistance: Acid')
                self.raceAbilityDisc.append('Acid Breath 5 by 30 ft. line')
            elif self.color == 'gold':
                self.raceAbility.append('Fire Breath')
                self.raceAbility.append('Damage Resistance: Fire')
                self.raceAbilityDisc.append('Fire Breath  15 ft. cone')
            elif self.color == 'green':
                self.raceAbility.append('Poison Breath')
                self.raceAbility.append('Damage Resistance: Poison')
                self.raceAbilityDisc.append('Poison Breath  15 ft. cone')
            elif self.color == 'red':
                self.raceAbility.append('Fire Breath')
                self.raceAbility.append('Damage Resistance: Fire')
                self.raceAbilityDisc.append('Fire Breath  15 ft. cone')
            elif self.color == 'silver':
                self.raceAbility.append('Cold Breath')
                self.raceAbility.append('Damage Resistance: Cold')
                self.raceAbilityDisc.append('Cold Breath  15 ft. cone')
            elif self.color == 'white':
                self.raceAbility.append('Cold Breath')
                self.raceAbility.append('Damage Resistance: Cold')
                self.raceAbilityDisc.append('Cold Breath  15 ft. cone')
            self.raceAbilityDisc.append('Damage Resistance: You have Resistance to the damage type associated with your draconic ancestry.')
        if self.race == 'human':
            self.raceAbility.append('None')
        if self.race == 'elf':
            self.raceAbility.append('Dark Vision')
            self.raceAbilityDisc.append('Darkvision: Accustomed to twilit forests and the night sky, you have superior vision in dark and dim Conditions. You can see in dim light within 60 feet of you as if it were bright light, and in Darkness as if it were dim light. You can’t discern color in Darkness, only shades of gray.')
            self.raceAbility.append('Fey Ancestry')
            self.raceAbilityDisc.append('Fey Ancestry: You have advantage on saving throws against being Charmed, and magic can’t put you to sleep.')
            self.raceAbility.append('Trance')
            self.raceAbility.append('Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After Resting in this way, you gain the same benefit that a human does from 8 hours of sleep.')

    # basic stats for race
    def setBasicRaceStats(self):
        if self.race.lower() == 'human':
            # humans have a +1 to ability scores
            if self.strength <= 19:
                self.strength += 1
            if self.dexterity <= 19:
                self.dexterity += 1
            if self.intellegence <= 19:
                self.intellegence += 1
        if self.race.lower() == 'dragonborn' or self.race.lower() == 'dragon born':
            # dragonborn have a +2 to Str score and +1 Charisma
            if self.charisma <= 19:
                self.charisma += 1
            if self.strength <= 19:
                self.strength += 1
        if self.race.lower() == 'elf':
            # elfs have a +2 to their dexterity score
            if self.dexterity <= 18:
                self.dexterity += 2
            else:
                self.dexterity = 20

    # set the hpDice for Character
    def setHpDice(self, dice):
        self.hpDice = dice

    def startLevel(self, level):
        self.charLevel = level

    def getHealthLevelUp(self, level):
        tempVar = 0
        print('You have leveled up !')
        while level > 0:
            tempVar = random.randint(0,self.hpDice)
            if(tempVar > self.hpDice/2):
                print('You rolled a: ',tempVar,' on a ',self.hpDice,'sided dice.')
                self.setMaxHealth(tempVar+self.max_health)
                self.setHealth(self.max_health)
                print('Your max health is: ',self.getMaxHealth(),' and your current health is: ',self.getHealth())
                level -= 1
            else:
                print('You rolled a: ', tempVar, ' on a ', self.hpDice, 'sided dice. Which is less than half +1 so you are getting a default increase of: ',self.hpDice/2+1,' amount of health')
                self.setMaxHealth(self.hpDice/2+1+self.max_health)
                self.setHealth(self.max_health)
                level -= 1

    # set what path you want to choose as a barbarian
    def initializePrimalPath(self):
        tempInput = ''
        # open up a file containing the paths of the barbarian
        with open("Barbarian_Paths.txt") as f:
            for line in f:
                time.sleep(2)
                print(line)
        # initialize x for the while loop
        x = 0
        y = 0
        print('Please choose what path you are going down. (berserker or totem warrior)')
        while x == 0:
            tempInput = input('').lower()
            if tempInput == 'berserker':
                self.path = tempInput
                x= 1
            elif tempInput == 'totem warrior':
                self.path = tempInput
                self.pathFeatures.append('Spirit Seeker')
                print('What animal will you choose? (bear, eagle or wolf)')
                while y == 0:
                    tempInput = input('').lower()
                    if tempInput == 'bear':
                        self.pathFeatures.append('bear')
                        y = 1
                    if tempInput == 'eagle':
                        self.pathFeatures.append('eagle')
                        y = 1
                    if tempInput == 'wolf':
                        self.pathFeatures.append('wolf')
                        y =1
                x= 1
            else:
                print('You entered an invalid path')

    # initialize the bard college path

    def setPrimalPath(self, path):
        x = 0
        tempInput = ''
        if path == 'berserker':
            if self.charLevel == 6:
                self.pathFeatures.append('Mindless Rage')
            elif self.charLevel == 10:
                self.pathFeatures.append('Intimidating Presence')
            elif self.charLevel == 14:
                self.pathFeatures.append('Retaliation')
        elif path == 'totem worrior':
            if self.charLevel == 6:
                print('Please choose one of the three spirit animals: bear, eagle or wolf.')
                # printing out the options that can be chose from.
                with open("Aspect of the Beast.txt") as f:
                    for line in f:
                        time.sleep(1)
                        print(line)

                while x == 0:
                    tempInput = input().lower()
                    if tempInput == 'bear':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    elif tempInput == 'eagle':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    elif tempInput == 'wolf':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    else:
                        print('The animal you chose is invalid.')
            if self.charLevel == 10:
                    self.pathFeatures.append('Spirit Walker')
            if self.charLevel == 14:
                print('Please choose one of the three spirit animals: bear, eagle or wolf.')
                # printing out the options that can be chose from.
                with open("Totemic Attunement.txt") as f:
                    for line in f:
                        time.sleep(1)
                        print(line)
                # asking for input but also making sure that they entered right animal
                while x == 0:
                    tempInput = input().lower()
                    if tempInput == 'bear':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    elif tempInput == 'eagle':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    elif tempInput == 'wolf':
                        self.pathFeatures.append(tempInput)
                        x = 1
                    else:
                        print('The animal you chose is invalid.')

    def getLevel(self):
        return self.charLevel

    # set the Character's class
    def setClass(self, Class, level):
        x = 0
        self.charClass = Class
        self.startLevel(level)
        # checking what class you are
        if self.charClass == 'barbarian':
            # adding what your saving throws are
            del self.savingThrow[:]
            self.savingThrow.append('Strength')
            self.savingThrow.append('Constitution')
            # setting the hpDice for Character
            self.setHpDice(12)
            # checking for what level the character is
            if self.charLevel == 1:
                # setting staring health of character
                self.setHealth(12 + self.constitutionMod)
                self.setMaxHealth(12 + self.constitutionMod)
                # sets the proficiency of the character
                self.proficiency = 2
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 2
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds features to the Character
                self.features.append('Unarmored Defence')
                if self.armor == 0:
                    self.AC = 10+self.dexterityMod+self.constitutionMod
                else:
                    self.AC = self.armor
            elif self.charLevel == 2:
                # sets the proficiency of the character
                self.proficiency = 2
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 2
                # adds the rage dmg to the Character
                self.rageDmg = 2
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 3:
                # sets the proficiency of the character
                self.proficiency = 2
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 3
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 4:
                # sets the proficiency of the character
                self.proficiency = 2
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 3
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                # Ability score increase
                self.abilityScoreIncrease()
                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)

                # get Primal path
                self.initializePrimalPath()
            elif self.charLevel == 5:
                # sets the proficiency of the character
                self.proficiency = 3
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 3
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 6:
                # sets the proficiency of the character
                self.proficiency = 3
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)

                # Path feature set
                self.setPrimalPath(self.path)
            elif self.charLevel == 7:
                # sets the proficiency of the character
                self.proficiency = 3
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 8:
                # sets the proficiency of the character
                self.proficiency = 3
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 2
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 9:
                # sets the proficiency of the character
                self.proficiency = 4
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 10:
                # sets the proficiency of the character
                self.proficiency = 4
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')

                # Path feature set
                self.setPrimalPath(self.path)

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 11:
                # sets the proficiency of the character
                self.proficiency = 4
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 4
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 12:
                # sets the proficiency of the character
                self.proficiency = 4
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 5
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 13:
                # sets the proficiency of the character
                self.proficiency = 5
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 5
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 14:
                # sets the proficiency of the character
                self.proficiency = 5
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 5
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')

                # Path feature set
                self.setPrimalPath(self.path)

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 15:
                # sets the proficiency of the character
                self.proficiency = 5
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 5
                # adds the rage dmg to the Character
                self.rageDmg = 3
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 16:
                # sets the proficiency of the character
                self.proficiency = 5
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 5
                # adds the rage dmg to the Character
                self.rageDmg = 4
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 17:
                # sets the proficiency of the character
                self.proficiency = 6
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 6
                # adds the rage dmg to the Character
                self.rageDmg = 4
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')
                self.features.append('Brutal Critical 3')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 18:
                # sets the proficiency of the character
                self.proficiency = 6
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 6
                # adds the rage dmg to the Character
                self.rageDmg = 4
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')
                self.features.append('Brutal Critical 3')
                self.features.append('Indomitable Might')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 19:
                # sets the proficiency of the character
                self.proficiency = 6
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 6
                # adds the rage dmg to the Character
                self.rageDmg = 4
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')
                self.features.append('Brutal Critical 3')
                self.features.append('Indomitable Might')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            elif self.charLevel == 20:
                # sets the proficiency of the character
                self.proficiency = 6
                # deletes the features just in case
                del self.features[:]
                # adds the features of the class
                self.features.append('Rage')
                # adds max amount of rages to Character
                self.rage = 9999999999999
                # adds the rage dmg to the Character
                self.rageDmg = 4
                # adds more features to the Character
                self.features.append('Unarmored Defence')
                self.features.append('Reckless Attack')
                self.features.append('Danger Sense')
                self.features.append('Extra Attack')
                self.features.append('Fast Movement')
                self.features.append('Feral Instinct')
                self.features.append('Brutal Critical')
                self.features.append('Relentless Rage')
                self.features.append('Brutal Critical 2')
                self.features.append('Persistent Rage')
                self.features.append('Brutal Critical 3')
                self.features.append('Indomitable Might')
                self.features.append('Primal Champion')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
        elif self.charClass == 'bard':
            # adding what your saving throws are
            del self.savingThrow[:]
            self.savingThrow.append('Dexterity')
            self.savingThrow.append('Charisma')
            # setting the hpDice for Character
            self.setHpDice(8)
            # checking for what level the character is
            if self.charLevel == 1:
                # setting basic Health values
                self.setHealth(8 + self.constitutionMod)
                self.setMaxHealth(8 + self.constitutionMod)

                # set proficiency
                self.proficiency = 2

                # setting max cantrip slots
                self.maxCantripSlots = 2

                # setting max spell slots
                self.maxSpellSlots = 4

                # setting max 1st level spell slots
                self.firstSpellMax = 2

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
            if self.charLevel == 2:

                # set proficiency
                self.proficiency = 2

                # setting max cantrip slots
                self.maxCantripSlots = 2

                # setting max spell slots
                self.maxSpellSlots = 5

                # setting max 1st level spell slots
                self.firstSpellMax = 3

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
                self.features.append('Jack of All Trades')
                self.features.append('Song of Rest')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            if self.charLevel == 3:

                # set proficiency
                self.proficiency = 2

                # setting max cantrip slots
                self.maxCantripSlots = 2

                # setting max spell slots
                self.maxSpellSlots = 6

                # setting max 1st level spell slots
                self.firstSpellMax = 4

                # setting max 2nd level spell slots
                self.secondSpellMax = 2

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
                self.features.append('Jack of All Trades')
                self.features.append('Song of Rest')
                self.features.append('Bard College')
                self.features.append('Expertise')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            if self.charLevel == 4:
                # set proficiency
                self.proficiency = 2

                # setting max cantrip slots
                self.maxCantripSlots = 3

                # setting max spell slots
                self.maxSpellSlots = 7

                # setting max 1st level spell slots
                self.firstSpellMax = 4

                # setting max 2nd level spell slots
                self.secondSpellMax = 3

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
                self.features.append('Jack of All Trades')
                self.features.append('Song of Rest')
                self.features.append('Bard College')
                self.features.append('Expertise')

                # Ability score increase
                self.abilityScoreIncrease()

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            if self.charLevel == 5:
                # set proficiency
                self.proficiency = 3

                # setting max cantrip slots
                self.maxCantripSlots = 3

                # setting max spell slots
                self.maxSpellSlots = 8

                # setting max 1st level spell slots
                self.firstSpellMax = 4

                # setting max 2nd level spell slots
                self.secondSpellMax = 3

                # setting max 3rd level spell slots
                self.thirdSpellMax = 2

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
                self.features.append('Jack of All Trades')
                self.features.append('Song of Rest')
                self.features.append('Bard College')
                self.features.append('Expertise')
                self.features.append('Bardic Inspiration 2')
                self.features.append('Font of Inspiration')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)
            if self.charLevel == 6:
                # set proficiency
                self.proficiency = 3

                # setting max cantrip slots
                self.maxCantripSlots = 3

                # setting max spell slots
                self.maxSpellSlots = 9

                # setting max 1st level spell slots
                self.firstSpellMax = 4

                # setting max 2nd level spell slots
                self.secondSpellMax = 3

                # setting max 3rd level spell slots
                self.thirdSpellMax = 3

                # adding the features
                self.features.append('Spellcasting')
                self.features.append('Bardic Inspiration')
                self.features.append('Jack of All Trades')
                self.features.append('Song of Rest')
                self.features.append('Bard College')
                self.features.append('Expertise')
                self.features.append('Bardic Inspiration 2')
                self.features.append('Font of Inspiration')
                self.features.append('Countercharm')

                # this will increase the current health and max health of the Character
                self.getHealthLevelUp(1)

    def abilityScoreIncrease(self):
        x = 0
        tempInput = 0
        print('===========================================================================')
        print('Your Ability scores Improved !')
        print('You get 2 points to put into any of your abilities !')
        print('Select 0: Str, 1: Dex, 2: Con, 3: Int, 4: Wis, 5: Char, 6: Check Abilities.')
        while x != 2:
            tempInput = int(input())
            if tempInput == 0:
                # adds a point to the Str ability
                self.strength += 1
                # get the modifier change
                self.setStrengthMod(self.strength)
                # marks down that you used your points
                x += 1
            elif tempInput == 1:
                # adds a point to the Str ability
                self.dexterity += 1
                # get the modifier change
                self.setDexterityMod(self.dexterity)
                # marks down that you used your points
                x += 1
            elif tempInput == 2:
                # adds a point to the Con ability
                self.constitution += 1
                # get the modifier change
                self.setConstitutionMod(self.constitution)
                # marks down that you used your points
                x += 1
            elif tempInput == 3:
                # adds a point to the Int ability
                self.intellegence += 1
                # get the modifier change
                self.setIntellegenceMod(self.intellegence)
                # marks down that you used your points
                x += 1
            elif tempInput == 4:
                # adds a point to the Wis ability
                self.wisdom += 1
                # get the modifier change
                self.setWidsom(self.wisdom)
                # marks down that you used your points
                x += 1
            elif tempInput == 5:
                # adds a point to the Char ability
                self.charisma += 1
                # get the modifier change
                self.setCharismaMod(self.charisma)
                # marks down that you used your points
                x += 1
            elif tempInput == 6:
                print("Your ability scores are:\n", 'Str: ', self.strength, '\nDex: ', self.dexterity, '\nCon: ', self.constitution, '\nInt: ', self.intellegence, '\nWis: ', self.wisdom, '\nChar: ', self.charisma)
            else:
                print('You entered an invalid ability to increase.')

    def classFeatures(self):
        if self.charClass == 'barbarian':
            if 'Rage' in self.features:
                self.rageFeat = 1
            if 'Unarmored Defence' in self.features:
                if self.armor == 0:
                    self.AC = 10+self.dexterityMod+self.constitutionMod
                else:
                    self.AC = self.armor
            if 'Reckless Attack' in self.features:
                self.recklessFeat = 1
            if 'Danger Sense' in self.features:
                self.dangerFeat = 1
            if 'Extra Attack' in self.features:
                self.extraFeat = 1
            if 'Feral Instinct' in self.features:
                self.feralFeat = 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.health / self.max_health) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.health) + "/" + str(self.max_health)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                    __________________________________________________ ")
        print(bcolors.BOLD + self.name + "  " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    # gets teh attack chance
    def tryAttack(self):
        return(random.randint(1,20))+self.strengthMod

    # gets the attack roll
    def attack(self):
        return(random.randint(1, self.dmgDice)*self.dmg)

    def showAbilities(self):
        print(self.features)

    def setWeapon(self, wep):
        self.weapon = self.weaponList[wep]

    def setDmg(self, num):
        self.dmg = num

    def setDmgDice(self, num):
        self.dmgDice = num

    def takeDmg(self, dmg):
        self.health -= dmg

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
        # dmg dice
        self.dmgDice = 0
        # dmg
        self.dmg = 0
        # amount of abilities AI knows
        self.abilityNum = 0
        # the abilities
        self.abilities = []


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

    # take damage
    def takeDmg(self, dmg):
        self.health -= dmg

    def attack(self):
        return random.randint(1,self.dmgDice)*self.dmg

    def setDmgDice(self, dmg):
        self.dmgDice = dmg

    def setDmg(self, dmg):
        self.dmg = dmg

    def tryAttack(self):
        return random.randint(1,20)

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.health / self.max_health) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.health) + "/" + str(self.max_health)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                    __________________________________________________ ")
        print(bcolors.BOLD + self.name + "  " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def attackAbility(self):
        tempInt = random.randint(0,self.abilityNum)
        if tempInt != 0:
            if self.abilities[tempInt] == 'Acid Attack':
                return random.randint(1,8)
            elif self.abilities[tempInt] == 'Slam Attack':
                return random.randint(1,self.dmgDice)*self.dmg+2
            elif self.abilities[tempInt] == 'Fire Ball':
                return random.randint(1,8)+2

    def setAbilities(self, a):
        if a == 0:
            self.abilities.append('Acid Attack')
            self.abilityNum += 1
        elif a == 1:
            self.abilities.append('Slam Attack')
            self.abilityNum += 1
        elif a == 2:
            self.abilities.append('Fire Ball')
            self.abilityNum += 1

# the main function of the game
def main():
    print_slow("This is a game created by Adam Emricson\nLast time this was edited was Wednesday 29th 2017\nAnd this game will be a text based DnD style game.")
    tempInput = 5
    i = 0
    rolls = []
    finalRoll = []
    time.sleep(.6)
    cls()
    player = Player()
    player.setName(input('Please enter your characters name (what you want to be refrenced by.)'))
    # a while statement to get 6 rolls for your int, str, dex, con, wis, cha
    while i < 18:
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
        elif i == 11:
            finalRoll.append(max(rolls))
            del rolls [:]
        elif i == 14:
            finalRoll.append(max(rolls))
            del rolls [:]
        elif i == 17:
            finalRoll.append(max(rolls))
            del rolls [:]
        i += 1
    print_slow("The computer will roll 16 d20\'s and take the top 6 rolls for your stats.")
    print('')
    print_slow("Choose what your Strength stat will be. (To do this just tyoe in one of the numbers from the rolls.)")
    print('')
    print(finalRoll)
    i = 0
    while i == 0:
        tempInput = int(input())
        if tempInput in finalRoll:
            i = 1
        else:
            print('You entered an invalid number.')
    player.setStr(tempInput)
    finalRoll.remove(tempInput)
    i = 0
    print(finalRoll)
    print_slow('Now choose the stat you want for Dexterity.')
    print('')
    while i == 0:
        tempInput = int(input())
        if tempInput in finalRoll:
            i = 1
        else:
            print('You entered an invalid number.')
    player.setDex(tempInput)
    finalRoll.remove(tempInput)
    print(finalRoll)
    i = 0
    print_slow('Now choose the stat you want for Charisma.')
    print('')
    while i == 0:
        tempInput = int(input())
        if tempInput in finalRoll:
            i = 1
        else:
            print('You entered an invalid number.')
    player.setCharisma(tempInput)
    finalRoll.remove(tempInput)
    print(finalRoll)
    i = 0
    print_slow('Now choose the stat you want for Constitution.')
    print('')
    while i == 0:
        tempInput = int(input())
        if tempInput in finalRoll:
            i = 1
        else:
            print('You entered an invalid number.')
    player.setConstitution(tempInput)
    finalRoll.remove(tempInput)
    i = 0
    print(finalRoll)
    i = 0
    print_slow('Now choose the stat you want for Wisdom.')
    print('')
    while i == 0:
        tempInput = int(input())
        if tempInput in finalRoll:
            i = 1
        else:
            print('You entered an invalid number.')
    player.setWidsom(tempInput)
    finalRoll.remove(tempInput)
    i = 0
    print(finalRoll)
    # sets the last value as intellegence
    print('And your final stat for Intellegence is: ', finalRoll[0])
    player.setInt(finalRoll[0])

    # what race do you want to be ?
    print_slow('What race do you want to be?')
    print('')
    print_slow('human: Ability scores increase by 1 (Strength +1, Dexterity +1, Intellegence +1)\ndragonborn: Strength increase by +2 and Breath attack\nelf: Dexterity increase by +2, Advantage on charm resistance, Only need 4 hours of rest to fully restore rather than 8 hours.')
    print('')
    # while loop to make sure correct race is inputted
    while i ==0:
        tempInput = input().lower()
        if tempInput == 'human':
            player.setRace(tempInput)
            i = 1
        elif tempInput == 'dragonborn' or tempInput == 'dragonborn':
            player.setRace(tempInput)
            i = 1
        elif tempInput == 'elf':
            player.setRace(tempInput)
            i = 1
        else:
            print('Incorrect race')

    player.setBasicRaceStats()

    i = 0

    print_slow('What class do you want to be ?')
    print('')
    print_slow('barbarian')
    print('')
    # allows you to pick a class
    while i == 0:
        tempInput = input().lower()
        if tempInput == 'barbarian':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'bard':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'cleric':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'durid':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'fighter':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'monk':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'paladin':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'ranger':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == ' rouge':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'sorcerer':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'warlock':
            player.setClass(tempInput, player.getLevel())
            i = 1
        elif tempInput == 'wizard':
            player.setClass(tempInput, player.getLevel())
            i = 1
        else:
            print('You entered an invalid class.')
    print_slow('Pick a weapon:')
    weapons = ['Battleaxe', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer', 'Whip']
    print_slow('Battleaxe (1d8), Flail (1d8), Glaive (1d10), Greataxe (1d12), Greatsword (2d6), Halberd (1d10), Lance (1d12), Longsword (1d8(, Maul (2d6), Morningstar (1d8), Pike (1d10))')
    print('')
    print_slow('Rapier (1d8), Scimitar (1d6), Shortsword (1d6), Trident (1d6), War Pick (1d8), Warhammer (1d8), Whip (1d4)')
    print('')
    x = 1
    while x == 1:
        wep = input('Please choose a weapon type the exact name: ')
        if wep == 'Battleaxe':
            player.setWeapon(0)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Flail':
            player.setWeapon(1)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Glaive':
            player.setWeapon(2)
            player.setDmg(1)
            player.setDmgDice(10)
            x = 0
        elif wep == 'Greataxe':
            player.setWeapon(3)
            player.setDmg(1)
            player.setDmgDice(12)
            x = 0
        elif wep == 'Greatsword':
            player.setWeapon(4)
            player.setDmg(2)
            player.setDmgDice(6)
            x = 0
        elif wep == 'Halberd':
            player.setWeapon(5)
            player.setDmg(1)
            player.setDmgDice(10)
            x = 0
        elif wep == 'Lance':
            player.setWeapon(6)
            player.setDmg(1)
            player.setDmgDice(12)
            x = 0
        elif wep == 'Longsword':
            player.setWeapon(7)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Maul':
            player.setWeapon(8)
            player.setDmg(2)
            player.setDmgDice(6)
            x = 0
        elif wep == 'Morningstar':
            player.setWeapon(9)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Pike':
            player.setWeapon(10)
            player.setDmg(1)
            player.setDmgDice(10)
            x = 0
        elif wep == 'Rapier':
            player.setWeapon(11)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Scimitar':
            player.setWeapon(12)
            player.setDmg(1)
            player.setDmgDice(6)
            x = 0
        elif wep == 'Shortsword':
            player.setWeapon(13)
            player.setDmg(1)
            player.setDmgDice(6)
            x = 0
        elif wep == 'Trident':
            player.setWeapon(14)
            player.setDmg(1)
            player.setDmgDice(6)
            x = 0
        elif wep == 'War Pick':
            player.setWeapon(15)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Warhammer':
            player.setWeapon(16)
            player.setDmg(1)
            player.setDmgDice(8)
            x = 0
        elif wep == 'Whip':
            player.setWeapon(17)
            player.setDmg(1)
            player.setDmgDice(4)
            x = 0
        else:
            print('Invalid choice.')

    player.setCharismaMod(player.charisma)
    player.setStrengthMod(player.strength)
    player.setConstitutionMod(player.constitution)
    player.classFeatures()
    player.setWisdomMod(player.wisdom)
    player.setIntellegenceMod(player.intellegence)
    player.setDexterityMod(player.dexterity)
    time.sleep(2)
    cls()
    player.printChar()
    time.sleep(2)
    tempVar = random.randint(0,1)
    print_slow('You start to open your eyes, and there before you is an unfamiliar scene. Things straight out of a fantasy... Trees, bushes, and the giant circle in the sky that people rumored about... The Sun.')
    print('')
    print_slow('Your mind finally catching up to the scene that\'s in front of you, you are outside. Realizing this you start convulsing, grabbing your head with your hands muttering to yourself in almost chant-like words \'This must be a dream. No this is a nightmare...\'')
    print('')
    print_slow('Suddenly some rustling comes from the bush next to you.')
    print('')
    print_slow('=======================================================')
    print('')
    print(bcolors.FAIL+'Attack')
    print(bcolors.OKGREEN+'Run'+bcolors.ENDC)
    tempVar = 1
    tempInput = input('What do you want to do ?')
    if tempInput == 'Attack':
        # makes a monster object
        enemy = AI()
        # names the monster
        enemy.setName('Goblin')
        # sets the health and other stats of the monster
        enemy.setHealth(10)
        enemy.setAC(5)
        enemy.setMaxHealth(10)
        enemy.setStr(12)
        enemy.setDex(12)
        enemy.setInt(12)
        # sets the damage of the monster
        enemy.setDmg(1)
        enemy.setDmgDice(4)
        # adds the slam ability
        enemy.setAbilities(1)
        print('You encounter: A Goblin.')
        print('')
        print('You surprised the Goblin, take your turn.')
        end = 1
        player.get_stats()
        print('')
        enemy.get_enemy_stats()
        print('')
        while end == 1:
            print(bcolors.BOLD,player.getName(),bcolors.ENDC)
            print(bcolors.BOLD+bcolors.OKBLUE,'Actions:',bcolors.ENDC)
            print_slow(' 1.  Attack')
            print('')
            print_slow(' 2.  Abilities')
            print('')
            print_slow(' 3.  Items')
            print('')
            tempInput = int(input('Choose Action:'))
            if tempInput == 1:
                tryAttack = player.tryAttack()
                if tryAttack >= enemy.getAC():
                    tempAttack = player.attack()
                    print('You attacked ',enemy.getName(),' for ',tempAttack,' points of damage.')
                    enemy.takeDmg(tempAttack)
                    time.sleep(.5)
                else:
                    print('You rolled a ',tryAttack)
                    print('You missed.')
                    time.sleep(.5)
            elif tempInput == 2:
                player.showAbilities()
                time.sleep(.5)
            elif tempInput == 3:
                if player.getInventory() == '':
                    print('You have no items.')
                    time.sleep(.5)
                else:
                    print(player.getInventory())
                    time.sleep(.5)
            else:
                    print('Invalid action choose 1-3')
            if enemy.health > 0:
                tryAttack = enemy.tryAttack()
                if tryAttack >= player.getAC():
                    tempAttack = enemy.attack()
                    print(enemy.getName(),' Attacked for ',tempAttack,' damage.')
                    player.takeDmg(tempAttack)
                    time.sleep(.5)
                else:
                    print(enemy.getName(),' missed.')
                    time.sleep(.5)
            print('====================================================')
            time.sleep(.5)
            player.get_stats()
            time.sleep(.5)
            print('')
            enemy.get_enemy_stats()
            time.sleep(.5)
            if player.getHealth() <= 0:
                print('You died')
                end = 0
            if enemy.getHealth() <= 0:
                print('You slayed the ',enemy.getName())
                print('')
                tempInput = player.charClass
                player.setClass(tempInput, 2)
                time.sleep(2)
                player.printChar()
                time.sleep(.5)
                print_slow('As the goblin dies you notice that there is a slip of paper sticking out of his pocket...')
                print('')
                end = 0
    elif tempInput == 'Run':
        print_slow('You run away from the noise.')
        print_slow('As you run away you notice a note on the ground...')
        print('')
        print('')
    else:
        print_slow('Invalid action.')
    print_slow('The note says:')
    print('')
    print_slow('==============================================================================================')
    print('')
    print_slow('     You need to assassinate the human king tonight, the plans already in motion. We need to')
    print('')
    print_slow('finish this as soon as possible if we are going to save our town from that tyrant.')
    print('')
    print_slow('==============================================================================================')
    print('')
    print('')
    print_slow('1.)  Go after this group')
    print('')
    print_slow('2.)  Figure out where you are')
    print('')
    tempVar = 1
    while tempVar == 1:
        tempInput = int(input('Select a choice:'))
        if tempInput == 1 or tempInput == 0:
            tempVar = 0

    if tempInput == 1:
        print_slow('You decide to figure out who and what this group is. But you still don\'t know where you are... But north seems like a good choice.')
        print('')
        print_slow('You end up walking for what seems like half a day until you reach a small house nested besides a lake.')
        print('')
        print('')
        print_slow('1.)  Continue on ?')
        print('')
        print_slow('2.)  Investigate ?')
        print('')
        tempVar = 1
        while tempVar == 1:
            tempInput = int(input('Select a choice:'))
            if tempInput == 1:
                print_slow('You decided to continue on your way, but fate had other plans for you. While leaving a figure approaches you.')
                print('')
                print_slow('He runs up to you and pulls his dagger out \'If you want to cross your going to have to give me your gold.\'')
                print('')
                print_slow('Seeing as you have no gold you begin to tell him you don\'t have any. He doesn\'t buy it.')
                print('')
                enemy = AI()
                enemy.setName('Sasha')
                enemy.setHealth(25)
                enemy.setAC(6)
                enemy.setMaxHealth(25)
                enemy.setStr(14)
                enemy.setDex(10)
                enemy.setInt(10)
                enemy.setDmg(1)
                enemy.setDmgDice(4)
                print_slow('You encounter: Sasha.')
                print('')
                print('')
                end = 1
                player.get_stats()
                print('')
                enemy.get_enemy_stats()
                print('')
                while end == 1:
                    print(bcolors.BOLD,player.getName(),bcolors.ENDC)
                    print(bcolors.BOLD+bcolors.OKBLUE,'Actions:',bcolors.ENDC)
                    print_slow(' 1.  Attack')
                    print('')
                    print_slow(' 2.  Abilities')
                    print('')
                    print_slow(' 3.  Items')
                    print('')
                    tempInput = int(input('Choose Action:'))
                    if tempInput == 1:
                        tryAttack = player.tryAttack()
                        if tryAttack >= enemy.getAC():
                            tempAttack = player.attack()
                            print('You attacked ',enemy.getName(),' for ',tempAttack,' points of damage.')
                            enemy.takeDmg(tempAttack)
                        else:
                            print('You rolled a ',tryAttack)
                            print('You missed.')
                    elif tempInput == 2:
                        player.showAbilities()
                    elif tempInput == 3:
                        if player.getInventory() == '':
                            print('You have no items.')
                        else:
                            print(player.getInventory())
                    else:
                        print('Invalid action choose 1-3')
                    if enemy.health > 0:
                        tryAttack = enemy.tryAttack()
                        if tryAttack >= player.getAC():
                            tempAttack = enemy.attack()
                            print(enemy.getName(),' Attacked for ',tempAttack,' damage.')
                            player.takeDmg(tempAttack)
                        else:
                            print(enemy.getName(),' missed.')
                    print('====================================================')
                    player.get_stats()
                    print('')
                    enemy.get_enemy_stats()
                    if player.getHealth() <= 0:
                        print('You died')
                        end = 0
                        tempVar = 0
                    if enemy.getHealth() <= 0:
                        print('You slayed the ',enemy.getName())
                        print('')
                        tempInput = player.charClass
                        player.setClass(tempInput, 3)
                        time.sleep(2)
                        player.printChar()
                        player.setClass(tempInput, 4)
                        time.sleep(2)
                        player.printChar()
                        time.sleep(.5)
                        print('')
                        end = 0
                        tempVar = 0
            elif tempInput == 2:
                print_slow('You notice that there is dead bodies near by... The sights of these dead bodies awake you from your slumber The End.')
    elif tempInput == 2:
        print('You try and figure out where you are but you come up blank... Through the hours you spent pondering where you could possibly be you died to heat stroke, a blow to the head, dehydration, starvation and lack of mental processing power... The End')
    print('The End !')



# clear the screen or so to say
def cls(): print ("\n" * 50)

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)

main()

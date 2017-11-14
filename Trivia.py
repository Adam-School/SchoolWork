class questions():
    #init statement to make the basic variables
    def __init__(self):
        self.questions = []
        self.answers = []

    def setQuestion(self, quest):
        self.questions.append(quest)

    def setAnswer(self, ans):
        self.answers.append(ans)

    def getQuestions(self, quest):
        return self.questions[quest]

    def getAnswer(self,ans):
        return self.answers[ans]

def main():
    points1 = 0
    points2 = 0

    quest = questions()

    quests = []
    answers = []
    #make a list of answers
    answers = ['Emoji','Face Sticker','Person Face','Faces','Liquid Cyinide Display','Light Crystal Display','Light Circle Display',
               'Liquid Crystal Display','Real on Memory', 'Read on Memory','Read only Memory','Real Occulas Memory','Computer Disk Reads only Memory',
               'Computer Data Reads on Memory','Computer Data Right on Memory','Compact Disk Read Only Memory','Iron','Steel','Alumminum',
               'Copper','Hydrogen','Oxygen','Carbon','Iron','Atlantic Ocean','Pacific Ocean','Indian Ocean','Artic Ocean','June','August',
               'December','January','Sargasso Sea','Black Sea','Boltic Sea','Red Sea','Iron','Oxygen','Nitrogen','Hydrogen']
    #making questions into a list
    quests.append('What do you call the small image icons used to express emotions or ideas in digital communication?')
    quests.append('When referring to a computer monitor, what does the acronym LCD stand for?')
    quests.append('When talking about computer memory, what does the acronym ROM stand for?')
    quests.append('What do the letters in the acronym CD-ROM stand for?')
    quests.append('Which is the most abundant metal in the earths crust?')
    
    quests.append('What is the second most abundant element in the earths atmosphere?')
    quests.append('What is the worlds largest ocean?')
    quests.append('In what month is the Earth closest to the sun?')
    quests.append('What is the only sea on Earth with no coastline?')
    quests.append('What is the most abundant element in the earths atmosphere?')
    #sending the questions to b stored in the object in class
    for r in range(0,10):
        quest.setQuestion(quests[r])
    #sending the answers to be stored in the object in class
    for x in range(0,40):
        quest.setAnswer(answers[x])
    print('-----------------------------------------------------------------------------------------------------------')
    print('Player 1 you get 5 trivia questions !')
    print('Question 1:',quest.getQuestions(0))
    for r in range(0,4):
        print('Answer',r+1,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(0)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points1 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 2:',quest.getQuestions(1))
    for r in range(4,8):
        print('Answer',r-3,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(7)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points1 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 3:',quest.getQuestions(2))
    for r in range(8,12):
        print('Answer',r-7,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(10)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points1 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 4:',quest.getQuestions(3))
    for r in range(12,16):
        print('Answer',r-11,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(15)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points1 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 5:',quest.getQuestions(4))
    for r in range(16,20):
        print('Answer',r-15,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(18)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points1 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)

    print('You got',points1,'out of 5 !')

    print('-----------------------------------------------------------------------------------------------------------')
    print('Player 2 you get 5 trivia questions !')
    print('Question 1:',quest.getQuestions(5))
    for r in range(20,24):
        print('Answer',r-19,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(20)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points2 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 2:',quest.getQuestions(0))
    for r in range(24,28):
        print('Answer',r-23,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(25)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points2 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 3:',quest.getQuestions(0))
    for r in range(28,32):
        print('Answer',r-27,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(31)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points2 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 4:',quest.getQuestions(0))
    for r in range(32,36):
        print('Answer',r-31,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(32)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points2 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)
    print('-----------------------------------------------------------------------------------------------------------')
    print('Question 5:',quest.getQuestions(0))
    for r in range(36,40):
        print('Answer',r-35,':',quest.getAnswer(r))
    userAnswer = input('Please enter the exact name of the answer for full points: ')
    rightAnswer = quest.getAnswer(38)
    if userAnswer == rightAnswer:
        print('Congrats ! you got the question right')
        points2 += 1
    else:
        print('You got the wrong answer ! the correct answer was',rightAnswer)

    if points1 > points2:
        print('Player 1 beat Player 2')
    elif points2 > points1:
        print('Player 2 beat Player 1')
    else:
        print('Both Players tied')
main()


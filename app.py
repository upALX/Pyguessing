import random

points = 1000
numberKick = 0
numberKicks = 0
lifes = 0

print('Welcome to Pygessing!')

difficultChoice = int(
    input('Please, chooise a difficult: (1) Easy - 20 Lifes | (2) Medium - 10 Lifes | (3) Hard | 3 Lifes: '))

while(difficultChoice < 1 or difficultChoice > 3):
        difficultChoice = int(input('Hi, you insert {}. Please, insert a number between 1 at 3: )'.format(difficultChoice)))
        continue

if(difficultChoice == 1):
    lifes = 20
    print('You choice the difficult {} - Easy! You have {} lifes. Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice, lifes))
elif (difficultChoice == 2):
    lifes = 10
    print('You choice the difficult {} - Medium! You have {} lifes. Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice, lifes))
else:
    lifes = 3
    print('You choice the difficult {} - Hard! You have {} lifes. Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice, lifes))

for numberKicks in range(numberKicks, lifes):
    numberRight = random.randrange(1, 101) #Is here to make a random number every iteration
    print('You have {} kicks of {} kicks.'.format(numberKicks, lifes))
    print('')
    print('Your points: {}'.format(points))
    print('')
    numberKick = int(input('Please, kick a number between 1 and 100: '))

    while(numberKick <1 or numberKick > 100):
        print('Ops... You insert a number most bigger than 100 or smaller than 1.')
        numberKick = int(input('Please, kick a number between 1 and 100: '))
        continue

    numberKickRight = numberKick == numberRight
    numberkickWrongUp = numberKick > numberRight

    print('')

    if(numberKickRight):
        points = points + (numberKick - numberRight)
        print('Congrats!')
    elif(numberkickWrongUp):
        points = points - (numberKick - numberRight)
        print('Ops, you kick up!', numberRight)
    else:
        points = points + (numberKick - numberRight)
        print('Ops, you kick down!', numberRight)

print('')

if(points < 1000):
    print('The end! What a pit! You finished with {} less points than it started!'.format((1000 - points)))
else:
    print('Congrats! You finished with {} more than it started!'.format((1000 + points)))
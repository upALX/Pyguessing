import random
print('Welcome to Pygessing!')

numberRight = random.randrange(1, 101)
points = 1000
numberKick = 0
lifes = 0
difficultChoice = int(
    input('Please, chooise a difficult: (1) Easy - 20 Lifes | (2) Medium - 10 Lifes | (3) Hard | 3 Lifes'))

while(difficultChoice < 1 or difficultChoice > 3):
        difficultChoice = int(input('Hi, you insert {}. Please, insert a number between 1 at 3 :)'.format(difficultChoice)))
        continue

if(difficultChoice == 1):
    lifes = 20
    print('You choice the difficult {} - Easy! Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice))
elif (difficultChoice == 2):
    lifes = 10
    print('You choice the difficult {} - Medium! Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice))
else:
    lifes = 3
    print('You choice the difficult {} - Hard! Remember kick numbers between 1 and 100. Sucess!'.format(difficultChoice))

numberKick = int(input('Please, kick a number between 1 and 100: '))
numberKicks = 0

numberKickRight = numberKick == numberRight
numberkickWrongUp = numberKick > numberRight

if(numberKickRight):
    print('Congrats!')
elif(numberkickWrongUp):
    print('Ops, you kick up!', numberRight)
else:
    print('Ops, you kick down!', numberRight)




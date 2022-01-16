import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("choose a number (from 1 to 9) "))
    if (introString > number):
        print("Choose a lower number")
    elif (introString == number):
        print("Congratulations, you guessed the right number")
    else :
        print("Choose a higher number")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You Lose, the correct number is ", number)



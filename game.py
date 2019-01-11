import random

rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()
import random

# Awroken

MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True

print "Alright..."

while RUNNING:
    GUESS = raw_input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print "Wrong, too low."
    elif int(GUESS) > NUMBER:
        print "Wrong, too high."
    elif GUESS.lower() == "exit":
        print "Better luck next time."
    elif int(GUESS) == NUMBER:
        print "Yes, that's the one, %s." % str(NUMBER)
        if TRY < 2:
            print "Impressive, only %s tries." % str(TRY)
        elif TRY > 2 and TRY < 10:
            print "Pretty good, %s tries." % str(TRY)
        else:
            print "Bad, %s tries." % str(TRY)
        RUNNING = False
    TRY += 1
import random
import sys
import time

#Taken from https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing and slightly modified

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


print_slow("Welcome to the Monty Hall problem!")
print()
print_slow("In this problem, there are three doors. Behind one door is your dream car, behind the other two doors are goats (or something equally undesirable).")
print()
#Randomising which door has which prize
prizes = ["car", "goat", "goat"]
random.shuffle(prizes)

original_choice = int(input("Choose a door (1-3):"))
#Input validation
while original_choice > 3 or original_choice < 1:
    print_slow("Make sure you chooose a number between 1 and 3")
    print()
    original_choice = int(input("Choose a door (1-3):"))
    print()

original_choice = original_choice - 1

print_slow("Good choice!")
print()
i=0
while i < len(prizes):
    if prizes[i] == "goat" and i != original_choice:
        print_slow("What if I told you behind door ")
        print_slow(str(i+1))
        print_slow(" there is a goat?")
        print()
        break
    i = i + 1

for x in range(3):
    if x != i and x != original_choice:
        remaining_door = x

print_slow("Would you like to change your choice from ")
print_slow(str(original_choice+1))
print_slow(" to door ")
print_slow(str(remaining_door+1))
print_slow(" ?")
print()
wish_to_change = (input("(y/n)"))

if wish_to_change == "y":
    for n in range(3):
        if n != i and n != original_choice:
            new_choice = n
else:
    new_choice = original_choice

print_slow("Your original choice, door ")
print_slow(str(original_choice+1))
print_slow(" had a ")
print_slow(str(prizes[original_choice]))
print_slow(" behind it")
print()

print_slow("Your revised choice, door ")
print_slow(str(new_choice+1))
print_slow(" had a " )
print_slow(str(prizes[new_choice]))
print_slow(" behind it")
print()

print_slow("Believe it or not, changing your choice is the correct answer 66% of the time! For more info https://en.wikipedia.org/wiki/Monty_Hall_problem")
print_slow("For proof, (made by yours truly) have a look at my github: ")


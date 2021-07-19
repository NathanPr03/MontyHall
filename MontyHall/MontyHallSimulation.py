import random

print("Welcome to the Monty Hall simulation!")
print("This program proves that changing your choice after a goat being revealed is the correct choice. For more info https://en.wikipedia.org/wiki/Monty_Hall_problem")
print()
original_correct = 0
new_correct = 0
iterations = 0
while iterations <= 10000000:
    #Randomising which door has which prize
    prizes = ["car", "goat", "goat"]
    random.shuffle(prizes)

    original_choice = random.randint(0,2)

    i=0
    while i < len(prizes):
        if prizes[i] == "goat" and i != original_choice:
            #print("What if I told you behind door", i, "there is a goat?")
            break
        i = i + 1

    for x in range(3):
        if x != i and x != original_choice:
            remaining_door = x

    #print("Would you like to change your choice from", original_choice, "to door", remaining_door, "?")
    #print()
    wish_to_change = "y"

    if wish_to_change == "y":
        for n in range(3):
            if n != i and n != original_choice:
                new_choice = n
    else:
        new_choice = original_choice

    #print("Your original choice, door", original_choice, "had a", prizes[original_choice], "behind it")

    #print("Your revised choice, door", new_choice, "had a", prizes[new_choice], "behind it")

    if prizes[original_choice] == "car":
        original_correct = original_correct + 1
    elif prizes[new_choice] == "car":
        new_correct = new_correct + 1
    iterations = iterations + 1
print("Original choice was correct", original_correct, "many times")
print("Revised choice was correct", new_correct, "many times")


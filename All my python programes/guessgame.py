from termcolor import colored
import time
import random


won = False
Number =  int(random.randint(1,100))

print("\n\n\n\n Start: \n")
time.sleep(0.5)
print("\n\n\n Picking Number ... ")
time.sleep(1.5)
print("\n\n\nNumber Picked\n\n Now you guess it :D \n\n You have 5 guesses")

for x in range(5):
    if won == False :
        guess = int(input("Enter Value : "))
        if(guess > Number):
            if x <= 3:            
                print("Try Low \n")
        elif(guess < Number):
            if x <=3:
                print("Try High \n")
        elif(guess == Number):
            won = True
        else:
            print(" !! Something Wrong !! \n\n")

if won:
    time.sleep(2)
    print(f"\n\nComputer guess : {Number} \n Your guess : {guess}")
    print(colored("\n   ----  CONGRATULATIONS ----\n             You Won\n\n","green"))
else:
    time.sleep(2)
    print(colored(f"Number was : {Number}    :(  \n\nnBetter Luck Next time \U0001f600\n\n","red"))

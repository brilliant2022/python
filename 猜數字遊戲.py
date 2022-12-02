import random
import os
number=random.randint(1,200)
number_of_guess=1
print("Guess the number between 1 and 200")
guess=input()
guess=int(guess)
while(1<= guess<= 200):
    if(guess!= number):
        number_of_guess+=1
        if(guess>number):
            print("Your guess is too high")
            guess=input()
            guess=int(guess)
        elif(guess<number):
            print("Your guess is too low")
            guess=input()
            guess=int(guess)
    elif(guess==number):
        print(f"Your guess is right!\nYou guess {number_of_guess}times.")
        break;
os.system("pause")
              
    

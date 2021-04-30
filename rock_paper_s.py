import random
import time

answers=["Rock","Paper","Scissors"]
computer_ans=random.choice(answers)

#Game welcome i guess
print("Rock") ; time.sleep(0.5)
print("Paper") ; time.sleep(0.5)
print("Scissors") ; time.sleep(0.5)
print("Shoot!!!"); time.sleep(0.5)

#user input+computer option 
user_ans=str(input("Enter an option... Rock, Paper or Scissors:  "))
print("Computers option is " +  computer_ans )

#game logic 
if user_ans == computer_ans:
    print("It's a tie!")
elif user_ans == "Rock" and computer_ans == "Scissors":
        print("Rock smashes scissors")
elif user_ans == "Rock" and computer_ans=="Paper":
    print("Paper Covers Rock")
elif user_ans == "Paper" and computer_ans=="Rock":
    print("Paper covers rock")
elif user_ans=="Paper" and computer_ans=="Scissors":
    print("Scissors cuts Paper")
elif user_ans=="Scissors" and computer_ans=="Paper":
    print("Scissors cuts Paper")
elif user_ans=="Scissors" and computer_ans=="Rock":
    print("Rock smashes scissors")







     

















    










   



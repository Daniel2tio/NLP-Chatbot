import datetime as dt
import random

def systemtime(time_question):
    date = dt.datetime.now()
    if time_question == 'time':
        seconds = date.strftime("%S")
        minutes = date.strftime("%M")
        hours = date.strftime("%H")
        print(">> Senku: Would you like to know the time? It's %s:%s:%s now." % (hours, minutes, seconds))

def emotions():
    emotions = ['ヽ(@ u @)ノ ','ヽ(ˋ▽ˊ)ノ','°(°ˊoˋ°) ° ','┑(￣▽ ￣)┍ ','┑(￣u ￣)┍ ',
              '╮(╯３╰)╭ ','(￣ε ￣) ','乀(ˉεˉ乀) ','ㄟ(▔皿▔ㄟ) ', '(╬▔▽▔)b ',
              '⊙﹏⊙','∩ω∩','?ω?','≧ω≦','＞ω＜',
              '(O ^ ~ ^ O)','(O ^ ~ ^ O)','o(≧ω≦)o','(￣３￣)a','(~￣▽￣)~[] ',
              '↖(^ω^)↗','~@^_^@~','\\*^o^*//','∩__∩y','★~★',
              '(^_^)∠※','(*^?^*)','<(￣︶￣)>','(#￣▽￣#) ','︿(￣︶￣)︿']

    id = random.randint(0, len(emotions)-1)
    return emotions[id]


def calculate_age(age_question):
    if age_question == 'how old am i' or "my age":
        Year = int(input(" Please enter the year you were born "))
        Month = int(input(" Please enter the number of the month you were born.  For example 3 = March "))
        Day = int(input(" Please enter the day you were born "))

        DOB = dt.datetime(Year,Month,Day)
        Age = (dt.datetime.now() - DOB)
        print("You are " + str(Age.days) + " days old")
    
        convertdays = int(Age.days)
        AgeYears = int(convertdays/365)

        print("Or " + str(AgeYears) + " years old to be less precise!")

def rock_paper_scissors(rps_question):
    
 if rps_question == 'rock paper scissors':      
    while True:
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        possible_actions = [rock , paper, scissors]
        #print(f"\nYou chose {user_choice}, whereas, I chose {computer_choice}.\n ")
        user_choice = int(input(">> Senku: Choose 0 for Rock, 1 for Paper or 2 for Scissors."))
        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")
        else:
            print(possible_actions[user_choice])
        computer_choice = random.randint(0, 2)
        print(f"I chose: {computer_choice}!")
        print(possible_actions[computer_choice])
        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")
        replay = input(">> Senku: Want to play again? (y/n): ")
        if replay.lower() == "y":
            print(">> Senku: Get Ready to lose")
        else:
            print(">> Senku: No worries, I'll always be down for another game when you feel like it!")
            break
        
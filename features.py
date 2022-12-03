import datetime as dt
import random

def systemtime(time_question):
    date = dt.datetime.now()
    if time_question == 'time':
        seconds = date.strftime("%S")
        minutes = date.strftime("%M")
        hours = date.strftime("%H")
        print(">> Senku: Would you like to know the time? It's %s:%s:%s now." % (seconds, minutes, hours))

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
    if age_question == 'how old':
        Year = int(input(" Please enter the year you were born "))
        Month = int(input(" Please enter the number of the month you were born.  For example 3 = March "))
        Day = int(input(" Please enter the day you were born "))

        DOB = dt.datetime(Year,Month,Day)
        Age = (dt.datetime.now() - DOB)
        print("You are " + str(Age.days) + " days old")
    
        convertdays = int(Age.days)
        AgeYears = convertdays/365

        print("Or " + str(AgeYears) + " years old to be less precise!")
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
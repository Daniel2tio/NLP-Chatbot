from features import systemtime
from features import emotions
from names import name_input
from Preprocessing import correct
from names import name_response
from smalltalk import smalltalk_answers
from QnA import qna_response

if __name__ == '__main__':
    
    #true until user says bye 
    flag = True

    user_name = '(Unknown)'
    print(">> Senku: I'm Senku. Yeah, you heard me right. I am the smartest human on earth...or bot? WTF!.")
    print("           Please Enter 'bye' if you want to say good bye.")
    print("           May I have ur name? %s" %emotions())
    print('>> %s: ' %user_name, end=" ")
    user_input = input()
    if user_input == 'bye':
        flag = False
    else:
        user_name = name_input(user_input)
        if user_name.lower() == 'daniel abreu':
            print(">> Senku: Oh, u r my father! I love u! %s" %emotions())
        else:
            print(">> Senku: Hi, %s, what do you want? %s" %(user_name, emotions()))

    while(flag == True):
        print('>> %s: '%user_name, end=" ")
        user_input = input()
        user_input = user_input.lower()
        user_input = [correct(i) for i in user_input.split(' ')]
        user_input = (' ').join(user_input)
        if(user_input != 'bye'):

            #name management memory

            response = name_response(user_input, threshold = 0.9)
            if response != 'NOT FOUND':
                print(">> Senku: I have a good memory. YOU ARE %s %s" %(user_name,emotions()))
                continue

            #system time management

            if 'time' in user_input:
                systemtime('time')
                continue

            if  'today' in user_input:
                systemtime('today')
                continue
            
            #small talk management
            response = smalltalk_answers(user_input, threshold = 0.9)
            if response != 'NOT FOUND':
                print(">> Senku: " + response + ' ' + emotions())
                continue

            # small talk
            response = qna_response(user_input, threshold = 0.1)
            if response != 'NOT FOUND':
                print(">> Senku: " + response + ' ' + emotions())
            else:
                print(">> Senku: I'm sorry. I don't know. Check Stack Overflow %s"%emotions())
                continue
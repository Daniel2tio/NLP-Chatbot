import datetime as dt

def systemtime(time_question):
    date = dt.datetime.now()
    if time_question == 'time':
        seconds = date.strftime("%S")
        minutes = date.strftime("%M")
        hours = date.strftime("%H")
        print(">> Senku: Would you like to know the time? It's %s:%s:%s now." % (seconds, minutes, hours))
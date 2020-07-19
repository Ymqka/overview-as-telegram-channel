import datetime

def logger(msg):
    date = datetime.datetime.now()
    with open("logs.txt", 'a') as f:
        f.write(str(date)+' : '+ msg + '\n')
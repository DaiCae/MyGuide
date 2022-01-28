import datetime

def getNowDatetime():
    date = datetime.datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")
import datetime
#date=datetime.datetime(2021, 5, 7, 11, 59, 59)
date=datetime.datetime(2021, 5, 7, 12, 0, 1)

name='John'
hour=date.hour
def greet(name,date):
    if date.hour>=6 and date.hour < 12:
        return 'Good morning'+' '+ name
    elif date.hour >= 12 and date.hour<20:
        return 'Good afternoon'+' '+ name
    else:
        return 'Good night'+' '+ name
print(greet(name,date))
#print(greet(date=datetime.datetime(2021, 5, 7, 12, 0, 1), name="John"))
#print(greet(name="John", date=datetime.datetime(2021, 5, 7, 11, 59, 59)))
       


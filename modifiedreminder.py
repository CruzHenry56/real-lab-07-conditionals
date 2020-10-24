import datetime

now = datetime.datetime.now()

print(now.year, now.month , now.day , now.minute , now.second)

#now.hour = float(input("What time is it? (0-23) "))
if now.hour <= 5:
    print("It's early.You should be sleeping")
elif now.hour <=7:
    print("wake brew that coffee, hit the gym, and eat breakfest")
elif now.hour <=9:
    print("Time to get to work")
elif now.hour <=12:
    print("You should be working")
elif now.hour <=13:
    print("Take your lunch break!")
elif now.hour <=17:
    print("Do you feel the afternoon lull?")
elif now.hour <=19:
    print("Time to take a nice bike ride")
elif now.hour <=21:
    print("Gotta eat that dinner.")
elif now.hour <=23:
    print("Go to sleep and repeat.")
else:
    print("You didnt type an accetable value")

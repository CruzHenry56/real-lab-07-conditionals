usertime = float(input("What time is it? (0-23) "))
if usertime <= 5:
    print("It's early.You should be sleeping")
elif usertime <=7:
    print("wake brew that coffee, hit the gym, and eat breakfest")
elif usertime <=9:
    print("Time to get to work")
elif usertime <=12:
    print("You should be working")
elif usertime <=13:
    print("Take your lunch break!")
elif usertime <=17:
    print("Do you feel the afternoon lull?")
elif usertime <=19:
    print("Time to take a nice bike ride")
elif usertime <=21:
    print("Gotta eat that dinner.")
elif usertime <=23:
    print("Go to sleep and repeat.")
else:
    print("You didnt type an accetable value")

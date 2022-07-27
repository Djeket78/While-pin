# allow user > enter PIN > true
from os import system
correct_pin = 1234
wrong = True
n=1
system ('cls')
while wrong:
    user_pin = int(input("Enter pin: "))
    if user_pin == correct_pin:
        print("Yes!!!")
        wrong = False
    else:
        print("Wrong!!!")
    n=n+1
    if n==4:
        print('Try again after 15 minets')
        break

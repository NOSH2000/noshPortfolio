
import time


story1=''' "Oh man! I didn't get the job AGAIN!
    How can I make fast money for my gambling debts! They are gonna kill me. I am broke here, dying out of my mind, while the
    rich guys have it all. I wish there was a way I can rob one of them.
    It's a weekday... They're probably at work. Hmm..." "'''

print()
print()
print("THE IDIOTIC BREAK IN")
time.sleep(3)
print()
print()
print(story1)
print()
print("You decide to rob the mansion")
from random import randint
option=randint(1, 2)



if option == 1:
    print()
    print("You climb the pipe and enter the mansion through the window and open the first door you see")
    time.sleep(5)
    print()
    print('''Suddenly you notice the chair rocking back and forth. You turn around to see the owner staring at him with a gun in his hand. "Run, you DIE," he threatens.''')
    print()

    user1= input("Do you to run or stay? Type in 'run' or 'stay'  ")
    if user1 !="run" and user1 != "stay":
        while (user1 !="run" and user1 != "stay" ):
            user1= input("ERROR! Type in 'run' or 'stay' exactly the same way as given  ")

    print()
    if user1== "stay":
        print('"You are so busted, son!" The owner starts laughing hysterically')
        print()
        time.sleep(5)
        print("The owner ties you up tightly with a golden leather belt. He then goes on to call the police")
        print()
        time.sleep(5)
        print('You end up in jail for 7 years. THE END, THIS IS WHAT YOU GET FOR YOUR STUPIDITY')
        print()
        print()
    elif user1=="run":
        print("Gunshot!")
        print("You are dead! THE END, THIS IS WHAT YOU GET FOR YOUR STUPIDITY")
        print()
        print()



elif option == 2:
    print()
    print("You enter the mansion through the backdoor")
    print()

    user2 = input("Do you want steal food or a huge antique statue,Type in 'food' or 'statue' ")
    if user2 !="food" and user2 != "statue":
        while (user2 !="food" and user2 != "statue" ):
            user2 = input("ERROR! Type in 'food' or 'statue' exactly the same way as given  ")

    if user2 == "food":
        print()
        print("You chose to take the 23-Karat Gold Chocolate Bacon")
        print()
        time.sleep(4)
        print("You hear footsteps in a distance. You choose to immediately run out through the backdoor")
        print()
        print('''You leave happily and enjoy your 23-Karat Gold Chocolate Bacon. ''')
        print()
        time.sleep(5)
        print("However you get abducted on your way out by your debtors. THE END.")
        print()
        print()
    elif user2== "statue":
        print("You decided to steal the golden monkey statue with a weight of 500 kilograms")
        print()
        time.sleep(5)
        print("In an attempt to steal it, you don't realize the man standing right behind you")
        print()
        time.sleep(5)
        print("In complete shock, you drop the statue on your foot.")
        print()
        time.sleep(3)
        print('Before you could recover and run, the man headlocks you')
        print()
        time.sleep(3)
        print("He follows that by calling the police who then arrive to arrest you for 10 years")
        print()
        print("The End. Hopefully when you return, you won't steal again")
        print()
        print()

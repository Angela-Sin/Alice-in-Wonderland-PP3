def intro():
    print("You are Alice. You've fallen a rabbit hole into the strange and magical world of Wonderland")
    print("You must find your way home, but first, you must explore this curious place and face its many challenges.")
    print("GOOD LUCK!")

    def play():
    print("text text text")
    print("rules rules rules")
    print("GOOD LUCK!")
    print()
    print("Where would you like to go?")
    print()
    print("1.")
    print("2.")
    print("3.")
    
firstChoice = input("which path you prefere? (1/2/3): ")
if firstChoice == '1':
    print()
    choice1()
elif firstChoice == '2':
    print()
    choice2()
elif firstChoice == '3':
    print()
    choice3()

def choice1():
    print()

def choice2():
    print()

def choice3():
    print()


print(""" ____ _____  _    ____ _____    ____    _    __  __ _____ 
/ ___|_   _|/ \  |  _ \_   _|  / ___|  / \  |  \/  | ____|
\___ \ | | / _ \ | |_) || |   | |  _  / _ \ | |\/| |  _|  
 ___) || |/ ___ \|  _ < | |   | |_| |/ ___ \| |  | | |___ 
|____/ |_/_/   \_\_| \_\|_|    \____/_/   \_\_|  |_|_____|""")
startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N':
    print("Next time")
elif startGame == 'Y':
    play()

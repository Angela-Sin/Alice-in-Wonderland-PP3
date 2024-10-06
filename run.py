

def play():
    print("You are Alice. You've fallen a rabbit hole into the strange and magical world of Wonderland")
    print("You must find your way home, but first, you must explore this curious place and face its many challenges.")
    print("GOOD LUCK!")
    print()
    print("Where would you like to go?")
    print()
    print("1. Follow the White Rabbit")
    print("2. Visit the Mad Hatter's Tea Party")
    print("3. Enter the Queen of Hearts' Castle")
    


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

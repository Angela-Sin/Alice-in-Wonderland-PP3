

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
    


print("""     _    _ _            _                            
   / \  | (_) ___ ___  (_)_ __                       
  / _ \ | | |/ __/ _ \ | | '_ \                      
 / ___ \| | | (_|  __/ | | | | |                     
/_/   \_\_|_|\___\___| |_|_| |_| _                 _ 
\ \      / /__  _ __   __| | ___| | __ _ _ __   __| |
 \ \ /\ / / _ \| '_ \ / _` |/ _ \ |/ _` | '_ \ / _` |
  \ V  V / (_) | | | | (_| |  __/ | (_| | | | | (_| |
   \_/\_/ \___/|_| |_|\__,_|\___|_|\__,_|_| |_|\__,_|""")

print()
print()
print("""   _   /  |
       | \  \/_/
       \_\| / __              
          \/_/__\           .--='/~\\
   ____,__/__,_____,______)/   /{~}}}
   -,-----,--\--,-----,---,\'-' {{~}}
           __/\_            '--=.\}/
          /_/ |\\
               \/""")

startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N' or startGame == "n":
    print("Next time")
elif startGame == 'Y' or startGame == "y":
    play()



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
    
print("""Welcome to the Magical World of Wonderland!
Enter a world where the ordinary becomes extraordinary, and every turn is a new adventure! 
In this magical land, the curious and the brave are invited to join Alice on her whimsical 
journey through enchanted gardens, tea parties with unusual characters, and mind-bending 
mysteries.
Get ready to meet talking animals, mischievous Cheshire Cats, and a Queen who isn't afraid 
to shout, "Off with their heads!" As you navigate this fantastical world, your decisions 
will shape the story, revealing secrets and challenges around every corner.
Are you brave enough to follow the White Rabbit down the rabbit hole? Embrace the madness,
let your imagination run wild, and let the adventure begin!
Remember: in Wonderland, nothing is quite what it seems. Are you ready to find out what's
 behind the mirror?""")

print("""    _    _ _            _                            
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
print("""     _
        _   / /\\
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

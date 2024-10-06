
#Play function
def play():
    print("""You are Alice. You've fallen down a rabbit hole into the strange and magical
    world of Wonderland!" Your goal is to find your way home, but first, you must explore
    this curious place and face its many challenges.
    
    Wish you Good Luck Alice!""")
    print()
    print()
    print("1. Follow the White Rabbit")
    print("2. Visit the Mad Hatter's Tea Party")
    print("3. Enter the Queen of Hearts' Castle")

    choice = input("> ") #choice function
    if choice == "1":
        rabbit_house()
    elif choice == "2":
        tea_party()
    elif choice == "3":
        queen_castle()
    else:
        print("Invalid choice. Please choose again.")
        play()

#Rabbit house
def rabbit_house():
    print("""\nYou follow the White Rabbit to his home, which is in a small hole. You land
     softly in a dimly lit tunnel filled with curious objects.""")

#Mad Hatter's tea party
def tea_party():
    print("""\nYou arrive at the Mad Hatter's tea party and find yourself at a long table
     under a large tree, filled with teapots, cups and cakes.""")

#Queen castle
def queen_castle():
    print("""\nYou enter the Queen of Hearts' castle. The air is tense, and the Queen herself
     is approaching! There is a large courtyard where the Queen of Hearts plays croquet with live flamingos and hedgehogs.""")    

#Welcome text    
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

#Start game function
startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N' or startGame == "n":
    print("Next time")
elif startGame == 'Y' or startGame == "y":
    play()

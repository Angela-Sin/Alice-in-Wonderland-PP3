import sys
import time

a = 1

#Play function
def play_game():
    print()
    print()
    print("""You follow the White Rabbit down a winding path that leads to a small door
    hidden in the roots of a large tree. Curiosity prompts you to open it, and you find
    yourself in a dimly lit tunnel. The walls of the tunnel are lined with shelves
    filled with strange objects:
    clocks that tick backwards, bottles with the words "Drink Me" written on them,
    and mirrors that seem to reflect worlds other than your own. 
    
    What you would like to do?
    Try a drink (1) 
    Explore the tunnel (2)?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        explore_tunnel()
    else:
        print("Invalid choice. Please choose again.")
        play_game()

def drink_me():
    print("""You found the tiny bottle with the sign "Drink Me".You uncork the bottle and inhale the
    strange liquid. Feeling bold, you take a sip.
    Immediately, a warm sensation spreads through your body, and you begin to shrink! The tunnel
    and everything in it grow larger around you. Shelves full of unusual objects loom like towering
    buildings, and the once-narrow path stretches out like a vast road.
    You become so small that even the curious trinkets around you now resemble giant, otherworldly sculptures.
    The tunnel feels much more intimidating at this size, and the ticking sound grows louder, almost echoing.
    
    In your new, tiny size, you can now see hidden details in the tunnel's floors and walls - cracks and crevices
    you couldn't see before. In one of these cracks, you notice a small, shimmering key lying just out of reach.
    
    What you would like to do?
    Take the Key (1)
    Leave the Key (2).""")

    choice = input("> ") #choice function
    if choice == "1":
        take_key()
    elif choice == "2":
        leave_key()
    else:
        print("Invalid choice. Please choose again.")
        drink_me()

def take_key():
    print("""You decide to pick up the tiny key. Its golden glow beckons you,
    and though you’re not sure what it unlocks, you sense that it’s important.
    Holding it tightly in your tiny hand, you continue down the tunnel that stretches endlessly before you.

    After what feels like an eternity of walking, you come to a small door built into the wall.
    At your current size, the door looks just the right height for you. You try the key, and it
    fits perfectly! The door creaks open, revealing another room, dimly lit but filled with familiar features:
    mismatched furniture, crooked picture frames, and—most importantly—a small table with another bottle on it.

    This bottle, like the first, has a label, but this one says “Drink Me Again.”

    Hesitantly, but eager to return to your normal size, you take a sip of the liquid. The moment she touches your lips,
    the familiar warm feeling returns and you begin to grow! The world around you shrinks to normal as her body stretches
    upward, and soon you are back to your normal size.

    Looking around, you notice a much larger door in front of you - a real exit, tall and inviting. You walk through it,
    leaving the strange tunnel behind.

    You find yourself in a vast, wondrous garden, filled with impossibly large mushrooms, flowers that seem to
    speak in whispers, and paths leading in every direction. The air is sweet with the scent of strange flowers,
    and distant, colorful creatures flutter across the sky.

    You realize that you have escaped the tunnel, but the strange world you have entered is far from home.
    It seems both enchanting and dangerous, full of secrets waiting to be explored.""")

def leave_key():
    print("""You stare at the small, glimmering key in the crack of the tunnel floor,
    but for reasons you can’t quite explain, you decide to leave it behind.
    Perhaps it’s your curiosity leading you onward, or maybe you simply don’t realize the key’s significance.
    You continue down the tunnel, your small size making everything feel much more intimidating and vast.

    As you venture deeper, the tunnel twists and turns, never offering a way out. The ticking grows louder,
    and the air feels heavier like it’s closing in on you. Every corner you turn looks the same as the last,
    and the once curious objects on the shelves now seem menacing, like they’re watching you.

    Time passes, but you can’t tell how long. It feels like hours, days, maybe even longer. The walls feel tighter,
    the shadows longer. You try calling out again, but your voice is lost in the endless echo.

    Without the key, You are stuck in the tunnel, unable to find a way out. The door behind you has disappeared,
    and no other exits reveal themselves. The ticking clock is the only constant, marking time in a world that feels like it's stopped.

    Over time, the tunnel becomes your entire world — a strange, shifting place with no escape.
    The objects that once seemed curious now feel like permanent companions, and the shadows that dance on the walls never leave you alone.
    
    What will you do next?
    
    1: Explore the garden further?
    2: Look for the White Rabbit?
    3: Rest for a moment and observe?""")

    choice = input("> ") #choice function
    if choice == "1":
        take_key()
    elif choice == "2":
        leave_key()
    else:
        print("Invalid choice. Please choose again.")
        take_key()

def explore_tunnel():
    print("""A few steps in, and the door behind you slams shut. The tunnel narrows,
    and you feel the walls pressing in slightly. Your heartbeat quickens as you search
    for another exit, but the tunnel stretches forward, twisting in impossible ways.

    You attempt to retrace your steps, but the door behind you has vanished. You realize you are trapped
    in a room where the air is thick with the unsettling feeling that you are not alone. Shadows move in
    the dim light, and somewhere deep within the tunnel, you hear the faint ticking of a clock that you cannot see.

    Do you explore the tunnel further, searching for hidden mechanisms in the objects around you (1)?
    Or do you call for help (2)?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        call_for_help()
    else:
        print("Invalid choice. Please choose again.")
        explore_tunnel()
    


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
name = input("Please enter your name: ")
time.sleep(a)
print()
print("Hello, " + name + "! Happy to see you!")
time.sleep(a)
print()
print()

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
print()
print()
print("""             /\\
        _   / /\\
       | \  \/_/
       \_\| / __              
          \/_/__\           .--='/~\\
   ____,__/__,_____,______)/   /{~}}}
   -,-----,--\--,-----,---,\'-' {{~}}
           __/\            '--=.\}/
          /_/ |\\
              \/""")

#Start game function
startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N' or startGame == "n":
    print("""That's totally okay!
    Adventure games can be a real journey. If you change your mind,
    just let me know and we can dive back into the whimsical world of Wonderland!""")
elif startGame == 'Y' or startGame == "y":
    play_game()

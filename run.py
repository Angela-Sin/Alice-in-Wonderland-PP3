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
    clocks that tick backwards, bottles with the words "Drink Me" 
     _
    {_}
    |(|
    |=|
   /   \\
   |.--|
   ||  |
   ||  |    
   |'--|  
   '-=-' written on them,
    and mirrors that seem to reflect worlds other than your own. 
    
    What you would like to do?

    1:Try a drink? 
    2:Explore the tunnel?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        explore_tunnel()
    else:
        print("Invalid choice. Please choose again.")
        play_game()

#Play >>> Drink Me
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
    
      ooo,    .---.
     o`  o   /    |\________________
     o`   'oooo()  | ________   _   _)
    `oo   o` \    |/        | | | |
      `ooo'   `---'         "-" |_|

    What you would like to do?

    1: Take the Key 
    2: Leave the Key""")

    choice = input("> ") #choice function
    if choice == "1":
        take_key()
    elif choice == "2":
        leave_key()
    else:
        print("Invalid choice. Please choose again.")
        drink_me()

#Play >>> Drink Me >>> Take Key
def take_key():
    print("""You decide to pick up the tiny key. Its golden glow beckons you,
    and though you’re not sure what it unlocks, you sense that it’s important.
    Holding it tightly in your tiny hand, you continue down the tunnel that stretches endlessly before you.

              ____
             |  , =,( _________
             | ='  (VvvVvV--'
             |____(

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
    It seems both enchanting and dangerous, full of secrets waiting to be explored.
    
    What will you do next?
    
    1: Explore the garden further?
    2: Look for the White Rabbit?
    3: Rest for a moment and observe?""")

    choice = input("> ") #choice function
    if choice == "1":
        explore_garden()
    elif choice == "2":
        look_for_rabbit()
    elif choice == "3":
        rest_in_garden()
    else:
        print("Invalid choice. Please choose again.")
        take_key()

#Play >>> Drink Me >> Take Key >>> Look For Rabbit >>> End of the Game
def look_for_rabbit():
    print("""You wander through the magic garden, enchanted by the vibrant colors and strange,
    talking flowers. The garden seems alive with energy, every step revealing new wonders.
    As you move through the towering mushrooms and glowing blossoms, she catches a glimpse
    of white fur darting between the tall plants.

    Excited, you hurry forward and soon find yourself face-to-face with the White Rabbit.
    He’s standing by a large mushroom, anxiously checking his pocket watch, as always. 
    The moment he sees you, his eyes widen, though not with surprise this time. Instead,
    there’s a look of relief.

    "Oh, there you are! I've been looking for you everywhere," the Rabbit says in his
    hurried voice. "This garden can be quite a tricky place, but lucky for you, I know the way out."

    You smile, feeling a wave of relief herself. "Thank you! I’ve been trying to find a way
    home for what feels like forever."

    The Rabbit, always in a rush, nods quickly. “Yes, yes, no time to waste. Follow me!”

    He hops ahead, and You follow closely as they weave through the garden. The landscape
    around you shifts strangely, as if the plants are moving out of their way, and the path
    constantly changes beneath your feet. But the Rabbit seems to know exactly where to go,
    never hesitating as he turns sharp corners and ducks under arching flowers.

    After what feels like just a few minutes of walking, you reach the edge of the garden,
    where a large gate stands. Beyond it, you can see the familiar sight of your world:
    a calm meadow leading back to your home.

    The Rabbit stops at the gate and gestures toward it. “There’s your way home,” he says. 
    “Once you pass through, you’ll be back in your world. But remember, Wonderland has a way
    of calling you back, so don’t be surprised if you return someday.”

    You look at the gate, your heart filled with both gratitude and a strange sadness.
    Wonderland has been strange, confusing, and often challenging, but it’s also been 
    magical. Still, she knows it’s time to go.

    “Thank you, Rabbit,” you say warmly. “For everything.”

    The White Rabbit gives her a quick nod, checking his watch once more. “Oh dear,
    I’m late again. Best of luck, Alice! Until we meet again!”

    With a final wave, you step through the gate. As she does, the garden fades behind you,
    replaced by the familiar warmth of her world. The sky is bright, the grass soft beneath 
    your feet, and in the distance, you can hear the comforting sounds of home.

    You smile, knowing you are safe and sound, but with the memory of Wonderland forever in your heart.""")


#Play >>> Drink Me >> Take Key >>> Rest in the garden
def rest_in_garden():
    print("""You decide to sit and rest for a while on the soft grass of the clearing.
    The garden seems alive, and you sense that by rushing forward you may miss something
    important. As you settle in, the whispers fade into the background, leaving only the
    gentle rustling of leaves and the soft hum of the air around you.

    The longer you sit, the more the garden seems to open up. The flowers nearby shift their
    positions slightly, as if turning towards you, and their glow intensifies, casting an ethereal
    light over the area. The spiral tree in the center with three doors seems almost to breathe,
    its bark shimmering in soft waves.

    As you watch, small details become clear:

    * * The red door (with the clock symbol) seems to pulse faintly, almost as if in sync with 
    the ticking sound she heard earlier in the tunnel. * *

    * * The blue door (with the heart symbol) radiates a faint warmth, and she hears the distant
    echo of laughter, though she cannot tell whether it is joyful or sinister. * *
    
    * *Faint shimmers float around the green door (with the crown symbol), like a magical trail,
    and for a moment you notice something glittering in the air near it, like the edge of a golden crown. * *

    As you look at the doors, the whispers begin to return, but this time they feel different.
    It is as if the garden is trying to communicate with you - not in words, but in feelings.
    The red door evokes a sense of urgency, as if time is of the essence. The blue door evokes
    a sense of curiosity mixed with caution as if it holds deep and complex emotions. 
    The green door hints at power, authority, and something grandiose, but also unknown.

    The garden seems to be giving you a choice, but not in a hurry - it is waiting for you to decide.
    
    What will Alice do next?
    
    1: Open the red door?         .-.-.     Symbol
                             ((  (__I__)  ))
                               .'_....._'.
                              / / .12 . \ \\
                             | | '  |  ' | |
                             | | 9  /  3 | |
                              \ \ '.6.' / /
                               '.`-...-'.'
                                /'-- --'\          
   
     2: Open the blue door  ,-"-,-"-.        Symbol
                           (         )
                            ".     ."
                              "._." 
    
    3: Open the green door     <>           Symbol   
                             .::::.             
                         @\\/W\/\/W\//@         
                          \\/^\/\/^\//     
                           \_O_<>_O_/""")

    choice = input("> ") #choice function
    if choice == "1":
        red_door()
    elif choice == "2":
        blue_door()
    elif choice == "3":
        green_door()
    else:
        print("Invalid choice. Please choose again.")
        rest_in_garden()
    
    

#Play >>> Drink Me >>> Take Key >>> Explore Garden
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden
def explore_garden():
    print("""You step further into the garden, your curiosity drawing you deeper into this strange,
     beautiful world. The vibrant colors and strange shapes of the plants around you make everything
    seem surreal. Flowers with faces whisper to each other, and huge mushrooms tower over you like trees.

    As you walk down the winding path, you notice something strange - the deeper you go, the more the
    garden seems to shift and change. The sky above shimmers between bright daylight and dark twilight,
    as if time is out of whack. The air hums with a strange energy, and the plants seem to move slightly
    when you're not looking.

    A rustling sound suddenly catches your attention. Peering ahead, you notice something flickering
    between the huge leaves. It's fast, too fast for you to see clearly, but you catch a flash of white.
    Could it be the White Rabbit? Or something else entirely?

    As you move cautiously forward, you come upon a strange sight: a large table set for tea in the center
    of the garden, completely out of place among the wild greenery. The table is covered with mismatched
    cups and saucers, some overturned, others stacked precariously high. There are empty chairs around it,
    though one at the far end has its back to her.

                  _
                  _(_)_                          wWWWw   _
      @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
     @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
      @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\\
       /      Y       \|    \|/    /(_)    \|      |/      |
    \ |     \ |/       | / \ | /  \|/       |/    \|      \|/
    \\|//   \\|///  \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|// 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Just as you are about to investigate, a voice calls out from behind you. "You're late, you know!"

    You turn to see a familiar face - the Cheshire Cat. He is lounging lazily on the branch of a nearby tree,
    his wide grin glittering in the changing light.

    "Well, well, what a curious traveler we have here," the Cat purrs, his eyes twinkling mischievously.""")


# Play >>> Drink Me >>> Leave the Key (End of the Game)
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
    """)


#Play >>> Explore Tunnel
def explore_tunnel():
    print("""A few steps in, and the door behind you slams shut. The tunnel narrows,
    and you feel the walls pressing in slightly. Your heartbeat quickens as you search
    for another exit, but the tunnel stretches forward, twisting in impossible ways.

    You attempt to retrace your steps, but the door behind you has vanished. You realize you are trapped
    in a room where the air is thick with the unsettling feeling that you are not alone. Shadows move in
    the dim light, and somewhere deep within the tunnel, you hear the faint ticking of a clock that you cannot see.

    What will you do next?
    1: Explore the tunnel further, searching for hidden mechanisms in the objects around you?
    2: Or do you call for help?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        call_for_help()
    else:
        print("Invalid choice. Please choose again.")
        explore_tunnel()


#Play >> Explore Tunnel >> Call For Help
def call_for_help():
    print("""Feeling a mixture of frustration and determination, you decide to call for help again.
    Your voice echoes through the dim tunnel, bouncing off the walls as you shout, “Help! Is anyone there?”

    For a moment, everything is silent. Just when you’re starting to lose hope, you hear the familiar patter
    of little feet approaching you. The White Rabbit appears, his eyes wide with worry.

    “Oh my god! Oh my god! What have you gotten yourself into?” he exclaims, slightly out of breath. “You really
    shouldn’t be wandering around here. Follow me, I’ll show you the way home!”

    Reassured, you quickly follow the Rabbit as he hops nimbly through the twisting paths of the tunnel.
    He looks back at you, a mixture of urgency and excitement on his face.

    “Stay close! "This tunnel can be quite tricky if you don't know your way around," he calls, leading 
    you through narrow passages and around sharp corners. The ticking of the invisible clock seems to grow
    quieter as they move deeper into the tunnel, and the air feels lighter.

    After a few minutes of hurried travel, they reach a door that glows faintly at the end of a long, winding
    corridor. The White Rabbit stops, pushing it open with a flourish.

    "There! You're almost home!" he says, his voice full of encouragement.

    Beyond the door is a vibrant garden, similar to the one you saw earlier, but this one is bursting with color
    and life. Flowers bloom in every hue, and the air is filled with sweet scents. In the distance, you see a familiar
    path leading back to the entrance to your world.

    "Just follow this path, and you'll be back where you belong," the White Rabbit assures you. "But remember,
    Wonderland has a way of calling you back.
    
    What will you do next?
    
    1: Thank the White Rabbit and head home?
    2: Explore the garden a bit more?""")

    choice = input("> ") #choice function
    if choice == "1":
        go_home()
    elif choice == "2":
        explore_garden()
    else:
        print("Invalid choice. Please choose again.")
        call_for_help()

#Play >>> Explore Tunnel >> Call for Help >> Go Home (End of the Game)
def go_home():
    print("""You turn to the White Rabbit, gratitude shining in your eyes.
    “Thank you so much for your help!” you exclaim. “I wouldn’t have found 
    my way without you!”

    The White Rabbit nods, adjusting his tiny vest. “Oh, nothing! Just doing my job,” he replies,
    looking back at the tunnel with a hint of worry. “But be careful out there. Wonderland can be
    quite unpredictable!”

    With one last wave, you walk through the door and onto the busy path that leads back to her world.
    The sun shines brightly overhead, illuminating the colorful flowers that seem to dance in the
    gentle breeze. You feel the warmth of the sunlight on her face, a calming reminder of home.

    As you walk, you pause for a moment to appreciate the beauty of the garden. Each flower is a riot
    of color, and a sweet scent fills the air. You notice butterflies fluttering about, their delicate
    wings sparkling like jewels in the sun. For a moment, you want to linger, to explore this magical
    place a little longer.

                      __ \/ __
     /\^/`\          /o \{}/ o\   
    | \/   |         \   ()   /     
    | |    |          `> /\ <`   ,,,     
    \ \    /  @@@@    (o/\/\o)  {{{}}                 _ _
     '\\//'  @@()@@  _ )    (    ~Y~       @@@@     _{ ' }_
       ||     @@@@ _(_)_   wWWWw .oOOo.   @@()@@   { `.!.` }
       ||     ,/  (_)@(_)  (___) OO()OO    @@@@  _ ',_/Y\_,'
       ||  ,\ | /)  (_)\     Y   'OOOO',,,(\|/ _(_)_ {_,_}
   |\  ||  |\\|// vVVVv`|/@@@@    _ \/{{}}}\| (_)@(_)  |  ,,,
   | | ||  | |;,,,(___) |@@()@@ _(_)_| ~Y~ wWWWw(_)\ (\| {{{}}
   | | || / / {{}}} Y  \| @@@@ (_)#(_) \|  (___)   |  \| /~Y~
    \ \||/ /\\|~Y~ \|/  | \ \/  /(_) |/ |/   Y    \|/  |//\|/
     `\\//`,.\|/|//.|/\\|/\\|,\|/ //\|/\|.\\\| // \|\\ |/,\|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    But her heart pulls you forward. You know you need to return to your world, to the familiar comfort
    of your home.

    As you walk along the path, you hear the soft sound of running water nearby. Curiosity piqued, you
    wander a little off the main path to see a small stream running through the garden, its waters
    sparkling like diamonds. It flows peacefully, meandering through the flowers and leading to the distant horizon.

    Suddenly, you realize you can’t stay.
    With one last look around, you return to the main path and continue on your way. Soon you reach the
    edge of the garden, where the flowers give way to a familiar landscape. The soft rolling hills, the 
    bright green grass, and the distant sound of her family calling her name fill you with joy.

    As you step through the door back into her world, you feel a sense of completion. She looks back one
    last time at Wonderland, the magical place that took you on an incredible adventure.

    “I will never forget you,” you whisper to the garden.

    With a deep breath, you step forward into your reality.

    Back in your garden, you hear the sounds of your family enjoying a lovely picnic. The aroma of freshly
    baked treats wafts through the air and laughter echoes around you.

    You smile, knowing that even though your adventure in Wonderland has come to an end, the memories will
    forever remain in your heart. And who knows? Perhaps one day you will return.""")

#Welcome
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
print("""    /\\
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

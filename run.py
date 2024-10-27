import sys
import time
import colorama
from colorama import Fore, Back, Style

a = 2

def type(text):
    words = text
    """
    Print text with a typing effect.
    """
    for char in words:
      time.sleep(0.01)
      sys.stdout.write(char)
      sys.stdout.flush()


def prompt_replay():
    """
    Function to restart the game
    """
    while True:
        print()
        type(f"{Fore.YELLOW} ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆ {Fore.RESET}\n")
        print()
        print()
        startGame = input('Would you like to dive back into the whimsical world of Wonderland? (Y/N): ').strip().lower()
        if startGame == 'n':
            print()
            print()
            type(f"{Fore.YELLOW} ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆{Fore.RESET}\n")
            print()
            print()
            type(f"""{Fore.MAGENTA}Thank you for joining Alice on her magical journey through Wonderland!
Your curiosity and choices brought the adventure to life, and we hope 
you had as much fun exploring as Alice did. Every step you took made 
Wonderland a little more wondrous.

Until we meet again, may your imagination always guide you to new 
adventures! Goodbye for now, and remember—Wonderland is never too 
far away.\n""")
            sys.exit()
            break
        elif startGame == "y":
            play_game()
            break
        else:
            print()
            print(f"{Fore.RED}Please enter a valid option: 'Y' or 'N'.{Fore.RESET}\n")
            time.sleep(a)

def play_game():
    """
    Beginning of the game.
    """
    print()
    type(f"""{Fore.YELLOW} You follow the White Rabbit down a winding path that 
leads to a small door hidden in the roots of a large tree. Curiosity 
prompts you to open it, and you find yourself in a dimly lit tunnel. 
The walls of the tunnel are lined with shelves filled with strange 
objects: clocks that tick backwards, bottles with the words "Drink Me" 
written on them, and mirrors that seem to reflect worlds other than 
your own.{Fore.RESET}            
    
    {Fore.BLUE}What you would like to do?{Fore.RESET}

    1:Try a drink? 
    2:Explore the tunnel?\n""")
    while True:
        choice = input(" >>>  ") #choice function
        if choice == "1":
            drink_me()
            break
        elif choice == "2":
            explore_tunnel()
            break
        else:
            print()
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n")  
        

def drink_me():
    """
    Steps:
    Play Game >> Drink Me
    """
    print()
    type(f"""{Fore.YELLOW}You found the tiny bottle with the sign "Drink Me".
You uncork the bottle and inhale the strange liquid. Feeling bold, 
you take a sip. Immediately, a warm sensation spreads through your 
body, and you begin to shrink! The tunnel and everything in it grow 
larger around you. Shelves full of unusual objects loom like towering 
buildings, and the once-narrow path stretches out like a vast road. 
You become so small that even the curious trinkets around you now 
resemble giant, otherworldly sculptures. The tunnel feels much more 
intimidating at this size, and the ticking sound grows louder, almost 
echoing.

In your new, tiny size, you can now see hidden details in the tunnel's 
floors and walls - cracks and crevices you couldn't see before. In one 
of these cracks, you notice a small, shimmering key lying just out of 
reach.{Fore.RESET}

      ooo,    .---.
     o`  o   /    |\\________________
     o`   'oooo()  | ________   _   _)
    `oo   o` \\    |/        | | | |
      `ooo'   `---'         "-" |_|
   
      

    {Fore.BLUE}What you would like to do?{Fore.RESET}

    1: Take the Key 
    2: Leave the Key\n""")

    while True:
        choice = input(" >>>  ") #choice function
        if choice == "1":
            take_key()
            break
        elif choice == "2":
            leave_key()
            break
        else:
            print()
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n")  
        

def take_key():
    """
    Steps:
    Drink Me >> Take key
    """
    print()
    type(f"""{Fore.YELLOW}You decide to pick up the tiny key. Its golden glow beckons you, 
and though you’re not sure what it unlocks, you sense that it’s important. 
Holding it tightly in your tiny hand, you continue down the tunnel that 
stretches endlessly before you.
            
              ____
             |  , =, _________
             | ='  (VvvVvV--'
             |____|

After what feels like an eternity of walking, you come to a small door 
built into the wall. At your current size, the door looks just the right 
height for you. You try the key, and it fits perfectly! The door creaks 
open, revealing another room, dimly lit but filled with familiar features: 
mismatched furniture, crooked picture frames, and—most importantly—a small 
table with another bottle on it.

This bottle, like the first, has a label, but this one says “Drink Me Again.”

Hesitantly, but eager to return to your normal size, you take a sip of the 
liquid. The moment it touches your lips, the familiar warm feeling returns 
and you begin to grow! The world around you shrinks to normal as your body 
stretches upward, and soon you are back to your normal size.

Looking around, you notice a much larger door in front of you - a real exit, 
tall and inviting. You walk through it, leaving the strange tunnel behind.

You find yourself in a vast, wondrous garden, filled with impossibly large 
mushrooms, flowers that seem to speak in whispers, and paths leading in 
every direction. The air is sweet with the scent of strange flowers, and 
distant, colorful creatures flutter across the sky.

You realize that you have escaped the tunnel, but the strange world you 
have entered is far from home. It seems both enchanting and dangerous, full 
of secrets waiting to be explored.{Fore.RESET}
    
      {Fore.BLUE}What will you do next?{Fore.RESET}
    
     1: Explore the garden further?
     2: Look for the White Rabbit?
     3: Rest for a moment and observe?\n""")

    while True:
        choice = input(" >>> ") #choice function
        if choice == "1":
            explore_garden()
            break
        elif choice == "2":
            look_for_rabbit()
            break
        elif choice == "3":
            rest_in_garden()
            break
        else:
            print()
            print(f"\n{Fore.RED}Invalid choice! Please enter '1', '2' or '3' {Fore.RESET}\n")  
            

def look_for_rabbit():
    """
    Steps:
    Take Key >> Look For Rabbit (End)
    Mad Hatter tea Party >> Look For Rabbit (End)
    """
    print()
    type(f"""{Fore.YELLOW}You wander through the magic garden, enchanted by the vibrant colors 
and strange, talking flowers. The garden seems alive with energy, every 
step revealing new wonders. As you move through the towering mushrooms 
and glowing blossoms, you catch a glimpse of white fur darting between 
the tall plants.{Fore.RESET}

                                        
                  {Fore.RED} _..._                      
                 ,' (_) `.                        
               .'   .-.   `.                       
              ,'_) :   : .-.\\                      
              .;-.   `-' (   )\\             
             (   )    _  `-'  ;             
              `-;_   (_)   ,-'              
                  `'------' {Fore.RESET}                
                   {Fore.WHITE}|    |                   
                   |    |
                  /     |       
                ,'      `.                       
                 `.    .//{Fore.RESET}              {Fore.LIGHTGREEN_EX})/{Fore.RESET}
                  {Fore.WHITE} `,-'{Fore.RESET}                {Fore.LIGHTGREEN_EX}(o))))))))<{Fore.RESET}

{Fore.YELLOW}Excited, you hurry forward and soon find yourself face-to-face with the 
White Rabbit. He’s standing by a large mushroom, anxiously checking his 
pocket watch, as always. The moment he sees you, his eyes widen, though 
not with surprise this time. Instead, there’s a look of relief.

"Oh, there you are! I've been looking for you everywhere," the Rabbit 
says in his hurried voice. "This garden can be quite a tricky place, 
but lucky for you, I know the way out."

You smile, feeling a wave of relief yourself. "Thank you! I’ve been 
trying to find a way home for what feels like forever."

The Rabbit, always in a rush, nods quickly. “Yes, yes, no time to waste. 
Follow me!”

He hops ahead, and you follow closely as you weave through the garden. 
The landscape around you shifts strangely, as if the plants are moving 
out of your way, and the path constantly changes beneath your feet. But 
the Rabbit seems to know exactly where to go, never hesitating as he 
turns sharp corners and ducks under arching flowers.

After what feels like just a few minutes of walking, you reach the edge 
of the garden, where a large gate stands. Beyond it, you can see the 
familiar sight of your world: a calm meadow leading back to your home.

The Rabbit stops at the gate and gestures toward it. “There’s your 
way home,” he says. “Once you pass through, you’ll be back in your world. 
But remember, Wonderland has a way of calling you back, so don’t be 
surprised if you return someday.”

You look at the gate, your heart filled with both gratitude and a strange 
sadness. Wonderland has been strange, confusing, and often challenging, 
but it’s also been magical. Still, you know it’s time to go.

“Thank you, Rabbit,” you say warmly. “For everything.”

The White Rabbit gives you a quick nod, checking his watch once more. 
“Oh dear, I’m late again. Best of luck, Alice! Until we meet again!”

With a final wave, you step through the gate. As you do, the garden fades 
behind you, replaced by the familiar warmth of your world. The sky is 
bright, the grass soft beneath your feet, and in the distance, you can 
hear the comforting sounds of home.

You smile, knowing you are safe and sound, but with the memory of 
Wonderland forever in your heart.{Fore.RESET}\n""")
    print() 
    prompt_replay()   


def rest_in_garden():
    """
    Steps:
    Take Key >>> Rest in the garden
    Explore Garden >>> Rest in the garden
    """
    print()
    type(f"""{Fore.YELLOW}You decide to sit and rest for a while on the soft grass of the 
clearing. The garden seems alive, and you sense that by rushing 
forward you may miss something important. As you settle in, the 
whispers fade into the background, leaving only the gentle rustling 
of leaves and the soft hum of the air around you.
{Fore.MAGENTA}
       ___
      / _ \\\\  ,,
     /=(_)=\\\\//
     \\ =(_) (O)
      \\_____\\\\      .--.     
       /=(_)\\\\\\   .'_\\/_'.  
       \\____///   '. /\\ .'   
            ()) {Fore.RESET}    {Fore.GREEN}"||"
                     || /\\\\    
                  /\\ ||//\)   
                 (/\\\\||/
        ____________\||/________________________________{Fore.RESET}

{Fore.YELLOW}The longer you sit, the more the garden seems to open up. The 
flowers nearby shift their positions slightly, as if turning 
towards you, and their glow intensifies, casting an ethereal light 
over the area. The spiral tree in the center with three doors 
seems almost to breathe, its bark shimmering in soft waves.

As you watch, small details become clear:

{Fore.RED}* * The red door (with the clock symbol) seems to pulse faintly, 
almost as if in sync with the ticking sound you heard earlier in 
the tunnel. * *{Fore.RESET}

{Fore.BLUE}* * The blue door (with the heart symbol) radiates a faint warmth, 
and you hear the distant echo of laughter, though you cannot tell 
whether it is joyful or sinister. * *{Fore.RESET}
    
{Fore.GREEN}* * Faint shimmers float around the green door (with the crown 
symbol), like a magical trail, and for a moment you notice 
something glittering in the air near it, like the edge of a 
golden crown. * *{Fore.RESET}

{Fore.YELLOW}As you look at the doors, the whispers begin to return, but this 
time they feel different. It is as if the garden is trying to 
communicate with you - not in words, but in feelings. The red 
door evokes a sense of urgency, as if time is of the essence. The 
blue door evokes a sense of curiosity mixed with caution as if it 
holds deep and complex emotions. The green door hints at power, 
authority, and something grandiose, but also unknown.

The garden seems to be giving you a choice, but not in a hurry - 
it is waiting for you to decide.{Fore.RESET}
    
    {Fore.BLUE}What will You do next?{Fore.RESET}
    
    1: Open the red door?\\n         
    2: Open the blue door?\\n 
    3: Open the green door?\\n""")

    while True:
        choice = input("  >>> ") #choice function
        if choice == "1":
            red_door()
            break
        elif choice == "2":
            blue_door()
            break
        elif choice == "3":
            green_door()
            break
        else:
            print()
            print(f"\n{Fore.RED}Invalid choice! Please enter '1', '2' or '3' {Fore.RESET}\n")   
        
    
def explore_garden():
    """
    Steps:
    Take Key >>> Rest in the garden
    Drink Me >>> Explore Garden
    Call For Help >>> Explore Garden 
    """
    print()
    type(f"""{Fore.YELLOW}You reached into the garden, your curiosity drawing you deeper into 
this strange, beautiful world. The vibrant colors and strange shapes 
of the plants around you make everything seem surreal. Flowers with 
faces whisper to each other, and huge mushrooms tower over you like 
trees.

As you walk down the winding path, you notice something strange - 
the deeper you go, the more the garden seems to shift and change. 
The sky above shimmers between bright daylight and dark twilight, 
as if time is out of whack. The air hums with a strange energy, 
and the plants seem to move slightly when you're not looking.

A rustling sound suddenly catches your attention. Peering ahead, you 
notice something flickering between the huge leaves. It's fast, too 
fast for you to see clearly, but you catch a flash of white. Could 
it be the White Rabbit? Or something else entirely?

As you move cautiously forward, you come upon a strange sight: a 
large table set for tea in the center of the garden, completely 
out of place among the wild greenery. The table is covered with 
mismatched cups and saucers, some overturned, others stacked 
precariously high. There are empty chairs around it, though one at 
the far end has its back to you.

                    _
                  _(_)_                         wWWWw   _
      @@@@       (_)@(_)  vVVVv     _     @@@@  (___) _(_)_ 
     @@()@@ wWWWw  (_)\\   (___)   _(_)_  @@()@@   Y  (_)@(_) 
      @@@@  (___)     `|/   Y    (_)@(_)  @@@@  \\|/   (_)\\  
       /      Y      \\|   \\|/    /(_)   \\|      |/      |  
     \\ |    \\ |/       | /\\ | / \\|/       |/   \\|     \\|/  
      \\|//   \\|///   \\|// \\|///\\|///   \\|//  \\|//   \\|//  
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just as you are about to investigate, a voice calls out from behind you. 
"You're late, you know!"

You turn to see a familiar face - the Cheshire Cat. He is lounging 
lazily on the branch of a nearby tree, his wide grin glittering in 
the changing light.

"Well, well, what a curious traveler we have here," the Cat purrs, 
his eyes twinkling mischievously.{Fore.RESET}
    
    {Fore.BLUE}What You will do next?{Fore.RESET}
    
    1: Talk to the Cheshire Cat
    2: Look for a way out of the garden\n""")

    while True:
        choice = input(" >>>  ") #choice function
        if choice == "1":
            talk_to_cat()
            break
        elif choice == "2":
            avoid_table()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n")  
        

def talk_to_cat():
    """
    Steps:
    Explore Garden >>> Talk to Cat
    """
    print()
    type(f"""{Fore.YELLOW}Lost again, are we?" the Cheshire Cat purrs, his grin widening. 
"You do have a habit of getting yourself into the most curious of 
predicaments, don't you?"

You, frustrated but trying to stay calm, look up at him. “Yes, I am 
lost,” you admit. “I’ve been wandering this strange place for too 
long. Can you show me the way home?”{Fore.LIGHTBLUE_EX}
          .'\\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
      `-._   ````    _.-'
          ``-------''{Fore.RESET}
{Fore.YELLOW}The Cheshire Cat tilts his head, his grin never fading. “Home? Hmm, 
now that’s a tricky thing to define here in Wonderland, isn’t it? 
What exactly is home? But... if you insist on leaving this 
delightful place, I might be persuaded to help.”

You watch him carefully, knowing the Cheshire Cat loves to toy with 
words and play tricks. “I just want to go back to where I came from,” 
you say firmly. “My world. Can you show me the way?”

The Cheshire Cat’s eyes twinkle with amusement. “Well, if that’s what 
you truly want, I can certainly point you in the right direction. 
But you must be careful. Wonderland has a way of holding onto its 
visitors, especially those with a curious mind like yours.”

With a slow stretch, the Cheshire Cat points his paw down one of the 
twisting paths behind him. “Follow that way, and you’ll come to a 
crossroads. Take the left path, and you’ll find a gate. Once you 
pass through it, you’ll be back in your world.”

He begins to fade away again, starting with his tail and ending with 
that ever-present grin. “But remember,” his voice lingers as he 
disappears completely, “the path you take may not always be the 
one you expect.”

You watch the Cheshire Cat vanish, a sense of both relief and 
uncertainty washing over you. Though his directions were vague, 
you had a way to go now.{Fore.RESET}
    
    {Fore.BLUE}What You will do next?{Fore.RESET}
    
    1: Follow the path Cat shows You?
    2: You tired and want to take a rest?
    3: Call Rabbit to find way home?\n""")

    while True:
        choice = input(" >>> ") #choice function
        if choice == "1":
            follow_cat()
            break
        elif choice == "2":
            rest_in_garden()
            break
        elif choice == "3":
            look_for_rabbit()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1', '2' or '3' {Fore.RESET}\n")  
        

def follow_cat():
    """
    Steps:
    Explore Garden >>> Follow cat (End)
    """
    print()
    type(f"""{Fore.YELLOW}You decide to trust the Cheshire Cat’s directions, even with the lingering
sense of mystery. You take a deep breath and head down the winding path he
pointed out, your heart beating a little faster with every step. The flowers
and plants around you seem to sway as if watching you, but you keep moving
forward, determined to find a way home.

After walking for a while, you come to a crossroads, just as the Cheshire
Cat had said. The left path looks slightly darker, shaded by towering trees,
but there’s a faint glow in the distance as if something important lies at
the end. Without hesitation, you turn left, your steps quicker now as you
feel you’re getting closer to the goal.

As you follow the path, the air grows warmer, and you can hear the sound of
wind rustling through the trees. In the distance, you spot a large gate,
golden and ornate, standing tall against the backdrop of the ever-shifting
Wonderland sky. The gate seems to shimmer, almost calling to you.

Your heart leaps — this must be the way home.

You approach the gate, and as you reach out to touch it, the latch clicks
open, almost on its own. Beyond the gate, you see a familiar sight: the
rolling green hills of your world, the soft, comforting colors of the
landscape you had been so eager to return to. The air smells fresher, and
the sky is the perfect shade of blue.

You step through the gate, leaving the curious world of Wonderland behind.
As you cross the threshold, you feel a strange, light sensation, as if the
weight of Wonderland’s madness is lifting from your shoulders. The gate
swings shut behind you with a soft click, and when you turn to look back,
there’s nothing but the peaceful meadow of your home.

With a sigh of relief, you know you are finally back.

The familiar sounds of your world surround you: birds singing, the gentle
breeze blowing through the grass, and the distant voices of your family
calling your name. You smile, feeling both exhausted and exhilarated. The
adventures of Wonderland are behind you now, but you know that the memories
will stay with you forever.

As you begin walking back toward your home, you wonder if you will ever
return to Wonderland. The Cheshire Cat’s words echo in your mind —
“Wonderland has a way of holding onto its visitors.” Perhaps one day, when
the time is right, you’ll find yourself back there again.

~~~~~~~~~~~~~~~~But for now, your home!~~~~~~~~~~~~~~~~~~~~{Fore.RESET}\n""")
    print()
    print() 
    prompt_replay() 

def avoid_table():
    """
    STeps:
    Explore Garden >>> Avoid Table (End)
    """
    print()
    type(f"""{Fore.YELLOW}You turn away from the tea table and the Cheshire Cat, deciding 
to follow one of the many twisting paths ahead. The garden seems 
to be full of possibilities, and your curiosity pulls you forward. 
You choose the nearest path, a narrow trail lined with glowing, 
luminescent flowers that seem to sway with you every step.

The path twists and turns, the garden growing wilder and stranger 
with every turn. The leaves overhead grow so thick that they almost 
block out the sky, creating a canopy that bathes the trail in dappled 
shadows. As you venture further, you hear faint whispers carried on 
the breeze. The voices seem to be coming from everywhere and nowhere 
all at once, but you can't quite make out what they're saying.

Soon, the path opens into a small, circular clearing. In the middle 
of the clearing stands a tall, spiraling tree with bark that shimmers 
in different colors as the light touches it. Its branches seem to 
reach out like arms, and at the base of the tree, there are three 
distinct doors carved into its trunk, each a different color: one red, 
one blue, and one green. Above each door, a symbol is etched: a clock, 
a heart, and a crown.

The whispers grow louder now as if the tree itself is speaking to you. 
The doors beckon, each promising a different path ahead.{Fore.RESET}

    {Fore.BLUE}What will You do next?{Fore.RESET}
    
    1: Open the red door?\\n
    2: Open the blue door?\\n
    3: Open the green door?\\n""")

    while True:
        choice = input(" >>>  ") #choice function
        if choice == "1":
            red_door()
            break
        elif choice == "2":
             blue_door()
             break
        elif choice == "3":
            green_door()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1', '2' or '3' {Fore.RESET}\n")   
        
 
def leave_key():
    """
    Steps:
    Drink Me >>> Leave the Key (End)
    """
    print()
    type(f"""{Fore.YELLOW}You stare at the small, glimmering key in the crack of the tunnel 
floor, but for reasons you can’t quite explain, you decide to leave 
it behind. Perhaps it’s your curiosity leading you onward, or maybe 
you simply don’t realize the key’s significance. You continue down 
the tunnel, your small size making everything feel much more 
intimidating and vast.

As you venture deeper, the tunnel twists and turns, never offering 
a way out. The ticking grows louder, and the air feels heavier like 
it’s closing in on you. Every corner you turn looks the same as the 
last, and the once curious objects on the shelves now seem menacing, 
like they’re watching you.

Time passes, but you can’t tell how long. It feels like hours, days, 
maybe even longer. The walls feel tighter, the shadows longer. 

You try calling out again, but your voice is lost in the endless echo.

Without the key, you are stuck in the tunnel, unable to find a way out. 
The door behind you has disappeared, and no other exits reveal 
themselves. The ticking clock is the only constant, marking time in a 
world that feels like it's stopped.

Over time, the tunnel becomes your entire world — a strange, shifting 
place with no escape. The objects that once seemed curious now feel 
like permanent companions, and the shadows that dance on the walls 
never leave you alone.{Fore.RESET}\n""")

    print()
    print() 
    prompt_replay() 



def explore_tunnel():
    """
    Steps:
    Play >>> Explore Tunnel
    """
    print()
    type(f"""{Fore.YELLOW}A few steps in, and the door behind you slams shut. The tunnel 
narrows, and you feel the walls pressing in slightly. Your heartbeat 
quickens as you search for another exit, but the tunnel stretches 
forward, twisting in impossible ways.

You attempt to retrace your steps, but the door behind you has vanished. 
You realize you are trapped in a room where the air is thick with the 
unsettling feeling that you are not alone. Shadows move in the dim light, 
and somewhere deep within the tunnel, you hear the faint ticking of a 
clock that you cannot see.{Fore.RESET}

    {Fore.BLUE}What will you do next?{Fore.RESET}

    1: Explore the tunnel further, searching for hidden mechanisms 
    in the objects around you?
    2: Or do you call for help?\n""")

    while True:
        choice = input(" >>>  ") #choice function
        if choice == "1":
            drink_me()
            break
        elif choice == "2":
            call_for_help()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n")  
        

def call_for_help():
    """
    Steps:
    Explore Tunnel >> Call For Help
    """
    print()
    type(f"""{Fore.YELLOW}Feeling a mixture of frustration and determination, you decide to 
call for help again. Your voice echoes through the dim tunnel, bouncing 
off the walls as you shout, “Help! Is anyone there?”

For a moment, everything is silent. Just when you’re starting to lose 
hope, you hear the familiar patter of little feet approaching you. The 
White Rabbit appears, his eyes wide with worry.

“Oh my god! Oh my god! What have you gotten yourself into?” he exclaims, 
slightly out of breath. “You really shouldn’t be wandering around here. 
Follow me, I’ll show you the way home!”

Reassured, you quickly follow the Rabbit as he hops nimbly through the 
twisting paths of the tunnel. He looks back at you, a mixture of urgency 
and excitement on his face.

“Stay close! This tunnel can be quite tricky if you don't know your way 
around," he calls, leading you through narrow passages and around sharp 
corners. The ticking of the invisible clock seems to grow quieter as you 
move deeper into the tunnel, and the air feels lighter.

After a few minutes of hurried travel, you reach a door that glows faintly 
at the end of a long, winding corridor. The White Rabbit stops, pushing it 
open with a flourish.

"There! You're almost home!" he says, his voice full of encouragement.

Beyond the door is a vibrant garden, similar to the one you saw earlier, 
but this one is bursting with color and life. Flowers bloom in every hue, 
and the air is filled with sweet scents. In the distance, you see a familiar 
path leading back to the entrance to your world.

"Just follow this path, and you'll be back where you belong," the White 
Rabbit assures you. "But remember, Wonderland has a way of calling you 
back."{Fore.RESET}
    
    {Fore.BLUE}What will you do next?{Fore.RESET}
    
    1: Thank the White Rabbit and head home?
    2: Explore the garden a bit more?\n""")

    while True:
        choice = input(">>>  ") #choice function
        if choice == "1":
            go_home()
            break
        elif choice == "2":
            explore_garden()
            break
        else:
           print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n") 
        

def go_home():
    """
    Steps:
    Explore Garden >>> Call for Rabbit (End)
    """
    print()
    type(f"""{Fore.YELLOW}You turn to the White Rabbit, gratitude shining in your eyes. 
“Thank you so much for your help!” you exclaim. “I wouldn’t have 
found my way without you!”

The White Rabbit nods, adjusting his tiny vest. “Oh, nothing! 
Just doing my job,” he replies, looking back at the tunnel with 
a hint of worry. “But be careful out there. Wonderland can be 
quite unpredictable!”

With one last wave, you walk through the door and onto the busy 
path that leads back to your world. The sun shines brightly 
overhead, illuminating the colorful flowers that seem to dance 
in the gentle breeze. You feel the warmth of the sunlight on 
your face, a calming reminder of home.

As you walk, you pause for a moment to appreciate the beauty of 
the garden. Each flower is a riot of color, and a sweet scent 
fills the air. You notice butterflies fluttering about, their 
delicate wings sparkling like jewels in the sun. For a moment, 
you want to linger, to explore this magical place a little 
longer.

But your heart pulls you forward. You know you need to return 
to your world, to the familiar comfort of your home.

As you walk along the path, you hear the soft sound of running 
water nearby. Curiosity piqued, you wander a little off the 
main path to see a small stream running through the garden, its 
waters sparkling like diamonds. It flows peacefully, meandering 
through the flowers and leading to the distant horizon.

Suddenly, you realize you can’t stay. With one last look 
around, you return to the main path and continue on your way. 
Soon you reach the edge of the garden, where the flowers give 
way to a familiar landscape. The soft rolling hills, the bright 
green grass, and the distant sound of your family calling your 
name fill you with joy.

As you step through the door back into your world, you feel a 
sense of completion. You look back one last time at Wonderland, 
the magical place that took you on an incredible adventure.

“I will never forget you,” you whisper to the garden.

With a deep breath, you step forward into your reality.

Back in your garden, you hear the sounds of your family enjoying 
a lovely picnic. The aroma of freshly baked treats wafts through 
the air, and laughter echoes around you.

You smile, knowing that even though your adventure in Wonderland 
has come to an end, the memories will forever remain in your 
heart. And who knows? Perhaps one day you will return.{Fore.RESET}""")
    print()
    print() 
    prompt_replay() 


def blue_door():
    """
    Steps:
    Rest in the Garden >> Blue Door
    Avoid Table >> Blue Door
    """
    print()
    type(f"""{Fore.YELLOW}You, drawn by curiosity, approach the blue door with the 
heart symbol etched above it. You hesitate for just a moment, 
then take a deep breath and open the door. A soft glow spills 
out, and without another thought, you step through.

As soon as you pass the threshold, the world around changes. 
You find yourself in a large, beautiful room with high ceilings, 
draped in rich blue and purple silks. The floor is a 
black-and-white checkerboard, and the air is filled with the 
scent of roses. In the distance, you can hear the soft 
tinkling of music, as if a grand ball is taking place 
somewhere nearby.

At the center of the room, a massive, ornate throne stands, 
with a heart-shaped crest at the top. And sitting on the 
throne is a figure that you immediately recognize — the 
Queen of Hearts.

The Queen’s sharp eyes fixed on you the moment you entered 
the room. "Ah, there you are," the Queen says with a mix of 
amusement and suspicion. "I wondered when you would find your 
way here. You’ve come through my door, so you must want 
something. Speak up, please!"

You take a cautious step forward. “I… I didn’t mean to intrude. 
I just followed the path and found this door.”

The Queen of Hearts raises an eyebrow, clearly unimpressed. 
"Didn’t mean to intrude? In Wonderland, everything has 
meaning, whether you know it or not. Now, what do you seek, 
here? Adventure? Answers? Or perhaps you’re here to challenge me?"

Your heart races. You remember the stories of the Queen’s 
temper, but also know that this might be your chance to learn 
something important — or perhaps even find a way home.{Fore.RESET}

    
    {Fore.BLUE}What will You do next?{Fore.RESET}
    
    1: Ask the Queen for help finding her way home?
    2: Challenge the Queen?
    3: Explore the room quietly, to look for an exit?\n""")

    while True:
        choice = input(" >>> ") #choice function
        if choice == "1":
            ask_queen()
            break
        elif choice == "2":
            challenge_queen()
            break
        elif choice == "3":
            explore_garden()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1', '2' or '3' {Fore.RESET}\n")   
        
    
def ask_queen():
    """
    Steps:
    Blue Door >> Ask Queen
    """
    print()
    type(f"""{Fore.YELLOW}You, feeling both nervous and hopeful, decide to speak to the 
Queen of Hearts directly. You know the Queen is a powerful 
figure in Wonderland, but you hope that by being polite, you 
might get the help you need to find your way home.

“Your Majesty,” you begin, bowing slightly, “I didn’t mean to 
disturb you, but I’ve been lost in Wonderland for quite some 
time now. I only wish to return to my world. Could you, 
perhaps, help me find my way home?”

The Queen of Hearts narrows her eyes for a moment, studying you. 
Her expression is unreadable, but after a long silence, the 
Queen’s lips curl into a small smile.

“Hmm… A bold request,” the Queen muses, tapping her fingers 
on the arm of her throne. “Most who come to Wonderland rarely 
wish to leave. But I suppose you are not most, are you?”

The Queen rises from her throne with a flourish of her red and 
gold robes. She steps down gracefully, her eyes still locked 
on you. “Very well. You’ve amused me, and I do so appreciate 
those with manners. I will help you — but only because it 
pleases me to do so.”

You feel a wave of relief, though you remain cautious, knowing 
the Queen’s temper could turn at any moment.

The Queen waves her hand, and suddenly, a small, ornate mirror 
appears floating in the air beside her. The frame is shaped 
like a heart and the glass shimmers with a strange light.

“This mirror,” the Queen says, “is a portal. It will show you 
the way back to your world. But remember, once you leave 
Wonderland, you may not be able to return as easily.”

You step closer to the mirror, your heart pounding with 
anticipation. “Thank you, Your Majesty,” you say sincerely. 
“I’m ready to go home.”

The Queen smirks. “Very well. Step through, and you shall find 
yourself where you belong.”

You take a deep breath, then reach out and touch the surface of 
the mirror. As soon as your fingers make contact, the glass 
ripples like water. You feel a strange pull, and before you 
know it, you are being gently drawn into the mirror.

The world around you swirls in a kaleidoscope of colors and 
lights, and for a brief moment, you feel weightless. Then, 
with a soft thud, you land on your feet.

When you open your eyes, you find yourself standing in a 
familiar meadow. The sky is bright, the air is warm, and in 
the distance, you can see home. You are back in your world.

You take a deep breath, filled with relief and wonder. Though 
your time in Wonderland had been full of strange and dangerous 
adventures, you were grateful for the experience. And though 
you are home now, you know that the magic of Wonderland will 
stay with you always.

With one last look at the horizon, you head home, your heart 
lighter and mind filled with memories of the incredible journey.{Fore.RESET}""")

    print() 
    prompt_replay() 

def challenge_queen():
    """
    Steps:
    Blue Door >> Challenge Queen (End)
    """
    print()
    type(f"""{Fore.YELLOW}You, feeling bold and defiant, straighten your back and look the 
Queen of Hearts in the eyes. You know the Queen can be dangerous, 
but you are no longer the same timid person who first stumbled 
into Wonderland. Your adventures have made you stronger, and if 
you have to stand up for yourself to get home, you are ready to 
do it.

“Your Majesty,” you begin, your voice steady, “I didn’t come here 
to beg for help. I’ve faced many challenges in Wonderland, and I’m 
not afraid of one more. If you want me to earn my way home, then 
I challenge you.”

The Queen of Hearts raises an eyebrow, clearly surprised by your 
boldness. For a moment, there’s silence in the grand throne room. 
Then, a slow smile spreads across the Queen’s face.

“A challenge, you say?” the Queen purrs, amused. “How delightful. 
I do love a good contest, especially when I’m confident I’ll win. 
But be warned, child — no one has ever beaten me in a challenge 
before.”

You hold your ground, determined. “I’ll take that risk.”

The Queen claps her hands and the room around them shifts. The 
walls seem to melt away, replaced by a vast arena with towering 
hedges and flickering lanterns. In the center stands a tall 
chessboard, its squares gleaming under the lights.

“We shall play a game,” the Queen declares. “A game of wits and 
strategy. If you win, I will grant you passage home. If you 
lose… well, I’m sure you can guess the consequences.”

The game begins and you quickly realize that the Queen is as clever 
as she is ruthless. The pieces move almost on their own, following 
subtle commands from the players. The Queen plays with precision, 
her knights and queens sweeping across the board with fierce intent.

But you, having learned to think quickly and cleverly in Wonderland, 
anticipate the Queen’s moves. She makes bold plays of her own, 
guiding her pieces with a combination of logic and intuition. The 
Queen’s frustration grows with each passing move, her confident 
smirk slowly fading.

Finally, after a tense series of moves, you see an opening. With 
a triumphant smile, you move your final piece into place and 
declare, “Checkmate.”

The Queen of Hearts freezes, staring at the board in disbelief. For 
the first time, someone has bested her. Her face flushes with 
anger, but instead of lashing out, she lets out a slow, controlled 
breath.

“Well, well,” the Queen says, her voice tight but controlled. “It 
seems you’ve won. I suppose I must honor my word.”

The chessboard vanishes, and the grand arena melts away, leaving 
you back in the throne room. The Queen waves her hand, and once 
again, the magical mirror appears, shimmering in the air beside her.

“This mirror will take you home,” the Queen says, though her tone 
is far less amused than before. “I suggest you take it before I 
change my mind.”

Your heart racing from the intensity of the game, you step toward 
the mirror. You look back at the Queen one last time, offering a 
polite but firm nod. “Thank you, Your Majesty.”

The Queen simply waves her off, her eyes smoldering but silent. 
Without wasting another second, you touch the surface of the mirror 
and feel the familiar pull.

In an instant, you are back in your world, standing in the same 
meadow where your adventure began. The sky is blue, the air fresh, 
and the sounds of Wonderland fade into distant memories. You are 
home at last.

You look around, your heart light and full of pride. You had stood 
up to the Queen of Hearts and won. Wonderland may have been strange, 
but it taught you that you were stronger and braver than you ever 
knew.

With a smile, you turn and begin to walk back home, knowing that 
you carry the lessons of Wonderland with you forever.{Fore.RESET}""")
    print()
    print()
    prompt_replay() 

def red_door():
    """
    Steps:
    Rest in the Garden >> Red Door
    Avoid Table >> Red Door
    """
    print()
    type(f"""{Fore.YELLOW}You take a deep breath, filled with curiosity and excitement, and push 
the red door open. As you step through, you feel a rush of cool air 
and a sense of wonder. The door closes softly behind you, and you 
find yourself in a vibrant, surreal landscape unlike anything you 
have ever seen.

The ground is covered in lush, colorful grass that seems to shimmer 
under a radiant sun. Giant mushrooms tower above you, their caps 
decorated with whimsical patterns. In the distance, you hear the 
sound of laughter and see a group of peculiar characters gathered 
around a large, crooked table, set for tea.

As you survey your surroundings, you notice:

A paved path leads to the tea party where the Mad Hatter and March 
Hare are celebrating with a peculiar assortment of teapots and 
pastries. A dark forest to your left, where strange, glowing 
creatures flit among the trees, inviting you to explore. A sparkling 
stream nearby, with a clear surface that reflects the colorful skies 
above.{Fore.RESET}

    {Fore.BLUE}What You will do next?{Fore.RESET}
    
    1: Join Mad Hatters Party?
    2: Go to Dark Forest?\n""")

    while True: 
        choice = input(" >>> ") #choice function
        if choice == "1":
            mad_hatter()
            break
        elif choice == "2":
            dark_forest()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n") 
        

def mad_hatter():
    """
    Steps:
    Red Door >> Mad Hatter
    """
    print()
    type(f"""{Fore.YELLOW}You, feeling a mix of excitement and nervousness, approach the Mad 
Hatter's tea party. The table is set with an array of colorful 
teapots, mismatched cups, and delectable pastries that seem to 
beckon you to join.

"Welcome, welcome!" the Mad Hatter exclaims, his eyes wide with 
enthusiasm. "Would you like some tea? We have every flavor 
imaginable, even ones you can't taste!"

You take a seat at the table, your curiosity piqued by the 
whimsical setup. The March Hare grins at you while nibbling on a 
scone, and the Dormouse stirs lazily in a teapot.

After a moment of enjoying the strange assortment of foods, you 
speak up. "Excuse me, Mr. Hatter, but I need your help. I’m trying 
to find my way home. Can you help me?"

The Mad Hatter pauses, his expression shifting to one of 
understanding. "Ah, home! A curious place indeed. But it seems 
you must first have a proper tea party with us!"

You nod eagerly, and they dive into a delightful and chaotic tea 
party filled with nonsensical conversations, laughter, and 
delightful treats. Time flies by as they share stories and 
riddles, and you momentarily forget your worries.

As the tea party comes to an end, you feel grateful for the 
laughter and joy but remember your goal. You turn to the Mad 
Hatter, who is tidying up the table.

"Thank you for the wonderful tea party! But now, could you please 
help me find my way home?" you ask earnestly.

The Mad Hatter grins, adjusting his large hat. "Of course, my dear! 
The way home is often hidden, but I can show you a path. Just 
follow the White Rabbit. He knows the way better than anyone 
else in Wonderland."

The March Hare adds with a wink, "Just look for him at the next 
intersection. He’ll be the one with the watch, of course—always 
running late!"

Your heart lifts at the thought of finally getting home. "Thank you 
so much! I’ll look for the White Rabbit!"

With a wave of your hand and a final farewell to your new friends, 
you set off from the tea party, following the winding path that 
the Mad Hatter pointed out. The landscape around you is filled 
with vibrant colors and peculiar sounds, but you stay focused on 
your mission.

As you walk, you begin to notice familiar landmarks—the large 
mushroom, the crooked tree, and finally, a little figure hopping 
in the distance. It’s the White Rabbit, glancing at his pocket 
watch with a worried expression.{Fore.RESET}


    {Fore.BLUE} What You will do next?{Fore.RESET}
     
     1: Call For the rabbit?
     2: Explore dark forest?\n""")

    while True:
        choice = input(" >>> ") #choice function
        if choice == "1":
            look_for_rabbit()
            break
        elif choice == "2":
            dark_forest_way_home()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice! Please enter '1' or '2'{Fore.RESET}\n") 
        

def dark_forest():
    """
    Steps:
    Red door >> Dark Forest (End)
    """
    print()
    type(f"""{Fore.YELLOW}You, curious and adventurous, decide to delve deeper into the dark 
forest rather than seek the White Rabbit. The trees loom tall above you, 
their twisted branches casting eerie shadows on the ground. The further 
you wander, the thicker the underbrush becomes, and the sounds of the 
outside world begin to fade away.

As you walk, the path becomes less defined, and you start to feel a sense 
of unease creeping in. The forest seems alive with whispers, rustling leaves, 
and distant echoes that make your heart race.

After what feels like hours of wandering, you realize you have strayed far 
from where you entered the forest. The tall trees block out the sunlight, 
and the air grows heavy with an unsettling silence.

“Oh no,” you mutter to yourself, “I should have followed the Rabbit.” You 
look around, hoping to find a familiar landmark, but everything seems to 
look the same: gnarled roots, towering trunks, and dense thickets of brambles.

Just then, you spot a flickering light in the distance, a soft glow that 
seems inviting. Feeling a glimmer of hope, you move towards it, thinking 
it might lead you back to safety.

As you approach the light, you discover it comes from a cluster of glowing 
mushrooms surrounded by swirling fog. They emit a soft, enchanting glow 
that dances in the dimness of the forest. Intrigued, you kneel to inspect 
them, wondering if they might be the key to finding your way back.

Suddenly, the fog thickens around you, and you feel a strange pull as if 
the forest is trying to envelop you. The enchanting glow becomes hypnotic, 
and you feel your resolve start to waver.

“What if I stay here for a while?” you muse, mesmerized by the mushrooms' 
light. “It could be fun to explore this magical place.”

As the fog wraps around you, your sense of time begins to dissolve. Hours 
blend into minutes and the concept of home slips from your mind. You wander 
deeper into the forest, captivated by its mysteries. You encounter strange 
creatures, hear melodies from hidden places, and dance with shadows.

But as days turn into weeks, you start to realize that you are not just 
exploring; you are lost. The forest has a life of its own, and its 
enchanting beauty has trapped you in a never-ending cycle of wonder.

Eventually, you sit beneath a great, ancient tree, feeling the weight of 
your decision. The reality of being lost sinks in, but you have grown fond 
of this magical world.

“This forest is my home now,” you whisper, a bittersweet smile gracing your 
lips. “I may never see my old life again, but this place is filled with 
wonders.”

And so, you become a part of the dark forest, a curious spirit wandering 
among the trees, forever enchanted by the magic that keeps you lost.{Fore.RESET}\n""")

    print()
    print()
    prompt_replay() 

def dark_forest_way_home():
    """
    Steps:
    Mad Hatter Party >> Dark forest way home (End)
    """
    print()
    type(f"""{Fore.YELLOW}After saying goodbye to the Mad Hatter and the March Hare, you decide 
to venture into the dark forest you had seen earlier. The trees are tall 
and twisted, their leaves forming a thick canopy that filters the sunlight 
into soft, dappled shadows on the ground.

As you walk deeper into the forest, you hear the gentle rustle of leaves 
and the distant sound of trickling water. The air is cool and fresh, and 
you feel a mix of excitement and apprehension. Suddenly, you spot a 
familiar figure darting between the trees—it’s the White Rabbit, looking 
just as flustered as ever.

“Excuse me! Mr. Rabbit!” you call out, your voice echoing through the 
forest.

The White Rabbit stops abruptly, his big ears twitching. He turns to face 
you, a look of relief washing over his face. “Oh, thank goodness! I thought 
I had lost you forever! I’ve been looking for you everywhere!”

You catch your breath, feeling a surge of hope. “I’m so glad to see you! I 
need your help to find my way home.”

The White Rabbit nods eagerly. “Of course! Follow me, and stay close. The 
way home can be tricky, but I know the path.”

As you make your way through the forest, the Rabbit leads you past twisted 
trees and sparkling streams. Along the way, he points out various landmarks, 
including peculiar flowers that giggle when touched and rocks that seem to 
hum a cheerful tune.

“This way!” the Rabbit exclaims, hopping ahead with surprising agility. You 
follow closely, your heart racing with anticipation.

After a short journey filled with laughter and surprises, you reach the edge 
of the dark forest. Ahead of you lies a beautiful meadow bathed in golden 
sunlight. At the far end of the meadow, you can see a shimmering portal that 
looks almost like a mirror.

The White Rabbit pauses and turns to you, his expression serious. “Beyond 
that portal lies your home. Just step through, and you will find yourself 
back where you belong.”

You gaze at the portal, your heart swelling with gratitude. “Thank you so 
much, Mr. Rabbit! I couldn’t have done this without you.”

“Just remember,” the Rabbit says with a wink, “you can always return to 
Wonderland if you follow your heart. Now go on!”

With a final wave, you step toward the shimmering portal. You feel a gentle 
tug as if the portal itself is welcoming you back. Taking a deep breath, you 
step through the mirror-like entrance.

Suddenly, you find yourself standing in your garden, the familiar sights and 
sounds of home enveloping you. The sun is shining brightly, and the flowers 
sway gently in the breeze.

“I’m home!” you exclaim, feeling a rush of joy wash over you. The adventure 
in Wonderland has come to an end, but the memories will stay with you 
forever.

As you walk through your garden, you can’t help but smile, knowing that you 
have discovered the magic of curiosity and friendship in a world where 
anything is possible.{Fore.RESET}\n""")
    print()
    print()
    prompt_replay() 

def green_door():
    """
    Steps:
    Rest in the Garden >> Green Door (End)
    Avoid Table >> Green Door (End)
    """
    print()
    type(f"""{Fore.YELLOW}With a spark of curiosity, you push open the vibrant green door and 
step inside. The door leads you into a lush, vibrant garden that feels 
alive with magic. The air is filled with the sweet scent of blooming 
flowers, and the gentle sound of rustling leaves creates a soothing melody.

As you wander further into the garden, you notice the enchanting scenery—
flowers of every color sway gracefully, and butterflies flit about, 
painting the air with their colorful wings. In the distance, you spot a 
familiar figure: it's the White Rabbit, looking just as hurried as ever.

"Ah, Alice!" the White Rabbit exclaims, his eyes wide with relief. "I was 
hoping to find you here! You seem to have quite a knack for getting lost."

You giggle, feeling a sense of warmth in seeing your friend again. “I’m 
glad to see you! I thought I’d never find you. I need help getting home."

The Rabbit adjusts his tiny waistcoat and peers around, his long ears 
twitching. "Follow me! There’s a secret path that leads right to your 
home, but you must be quick! The garden is enchanted, and time moves 
differently here."

Without another word, you follow the White Rabbit as he hops along a 
winding path through the garden. You pass by shimmering flowers and 
glowing streams, each step bringing you closer to the exit. The Rabbit 
glances back frequently, urging you to keep up.

“Just around this corner,” he says breathlessly, pointing to a cluster 
of trees that seem to shimmer in the sunlight. “There’s a doorway that 
will take you back.”

You reach a small archway covered in delicate vines, which leads to 
another door—this one painted a soft shade of blue. The Rabbit stops, 
catching his breath, and looks at you with a smile.

“Through this door is the way back home,” he assures you. “But remember, 
Alice, your adventures in Wonderland will always be here if you choose 
to return. Just keep your heart open to the magic around you.”

You nod, your heart racing with excitement and gratitude. “Thank you, 
Mr. Rabbit! I’ll always cherish my time here.”

With one last wave, you push open the blue door. You feel a rush of 
warmth and light engulf you as you step through.

Suddenly, you find yourself back in your familiar garden, the sun 
shining brightly overhead. The sounds of birds chirping and leaves 
rustling fill your ears, grounding you in the reality of your own world.

“I’m home!” you exclaim, your heart swelling with joy. The adventure in 
Wonderland has come to a close, but the memories of your whimsical 
journey and the friends you made will stay with you forever.

As you wander through your garden, you can’t help but smile, knowing 
that the magic of Wonderland is just a heartbeat away, ready for you 
to return whenever you wish.{Fore.RESET}\n""")
    print()
    print() 
    prompt_replay() 

# First Page
print(f"""{Style.BRIGHT}{Fore.LIGHTBLUE_EX}
                    ____     ____        {Fore.YELLOW}☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆{Fore.RESET}
                  {Fore.LIGHTBLUE_EX}/'    |   |    \\{Fore.RESET}      {Fore.YELLOW}☆{Fore.RESET}                    {Fore.YELLOW}☆{Fore.RESET}
                {Fore.LIGHTBLUE_EX}/    /  |   | \\   \\{Fore.RESET}     {Fore.YELLOW}☆{Fore.RESET} Alice's Adventure  {Fore.YELLOW}☆{Fore.RESET}
              {Fore.LIGHTBLUE_EX}/    / |  |'''|  \\   \\{Fore.RESET}    {Fore.YELLOW}☆{Fore.RESET}  In Wonderland!    {Fore.YELLOW}☆{Fore.RESET}
             {Fore.LIGHTBLUE_EX}(   /   |         |\\   \\{Fore.RESET}   {Fore.YELLOW}☆{Fore.RESET}                    {Fore.YELLOW}☆{Fore.RESET}
             {Fore.LIGHTBLUE_EX}| /   / /^\\    /^\\  \\  _|{Fore.RESET}   {Fore.YELLOW}☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆{Fore.RESET}
              {Fore.LIGHTBLUE_EX}~   | |   |  |   | | ~        
                  | |__O|__|O__| |
                /~~      \\/     ~~\\
               /   (      |      )  \\
         _--_  /,   \\____/^\\___/'   \\ _--_
       /~    ~\\ / -____-|_|_|-____-\\ /~    ~\\
     /________|___/~~~~\\___/~~~~\\ __|________\\
--~~~          ^ |     |   |     |  -     :  ~~~~~:~-_     ___-----~~~~~~~~|
   /             `^-^-^'   `^-^-^'                  :  ~\\ /'   ____/--------|
       --                                            ;   |/~~~------~~~~~~~~~|
 ;                                    :              :    |----------/--------|
:                     ,                           ;    .  |---\\--------------|
 :     -                          .                  : : |______________-__|
  :              ,                 ,                :   /'~----___________|
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Fore.RESET}\n""")

print()
player_name = input("Please enter your name >>> ")
print()
print(f"Hello {player_name.upper()}, Happy to see you!!! ")
time.sleep(a)
print()
print()

#Welcome text    
type("""Welcome to the Magical World of Wonderland!
Enter a world where the ordinary becomes extraordinary, 
and every turn is a new adventure! In this magical land, 
the curious and the brave are invited to join Alice on her
whimsical journey through enchanted gardens, tea parties with 
unusual characters, and mind-bending mysteries.
Get ready to meet talking animals, mischievous Cheshire Cats, 
and a Queen who isn't afraid to shout, "Off with their heads!"
As you navigate this fantastical world, your decisions 
will shape the story, revealing secrets and challenges around 
every corner. Are you brave enough to follow the White Rabbit 
down the rabbit hole? Embrace the madness,
let your imagination run wild, and let the adventure begin! 
Remember: in Wonderland, nothing is quite what it seems. 
Are you ready to find out what's behind the mirror?""")
print()
print()
print(f"""{Style.BRIGHT}{Fore.LIGHTGREEN_EX}
             /\\
        _   / /\\
       | \\\\/_/
       \\\\| / __{Fore.RESET}             
         {Fore.LIGHTGREEN_EX}\\/_/__\\{Fore.RESET}          {Fore.LIGHTRED_EX}.--='/~\\{Fore.RESET}
   {Fore.LIGHTGREEN_EX}____,__/__,_____,______){Fore.RESET}{Fore.LIGHTRED_EX}/    (~))){Fore.RESET}
   {Fore.LIGHTGREEN_EX}-,-----,--\\--,-----,---,{Fore.RESET}{Fore.LIGHTRED_EX}\'-'  ((~)){Fore.RESET}
          {Fore.LIGHTGREEN_EX} __/\\{Fore.RESET}            {Fore.LIGHTRED_EX}'--=.\\)/{Fore.RESET}
          {Fore.LIGHTGREEN_EX}/_/ |\\
             \\/  {Fore.RESET}\n""")

#Start game function
while True:
    startGame = input('Would You like to play? (Y/N):  ').strip().lower()
    if startGame == 'N' or startGame == "n":
        print()
        type(f"{Fore.YELLOW} ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆   ☆{Fore.RESET}\n")
        print()
        print()
        print("That's totally okay!")
        print()
        type("""Adventure games can be a real journey. If you change your mind, 
just let me know and we can dive back into the whimsical world 
of Wonderland!""")
        sys.exit()
        break
    elif startGame == 'Y' or startGame == "y":
        play_game()
        break
    else:
        print(f"{Fore.RED}Invalid choice! Please enter 'Y' for Yes or 'N' for No.{Fore.RESET}\n") 
    

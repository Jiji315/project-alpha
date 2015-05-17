# You can place the script of your game in this file.

# Declare images below this line, using the image statement.


# Declare characters used by this game.
define m = Character('Me', color="c8c8ff")
define l = Character('Lucas', color="#c8ffc8")
define c = DynamicCharacter("Strange Girl", color="#ff9900")
define g = DynamicCharacter("Quiet Girl", color="#99003")
define r = DynamicCharacter("Bookworm", color="#660099")
define h = DynamicCharacter("Gamer Girl", color="#0000ff")
define w = DynamicCharacter("Red-headed boy", color="ff5353")
define t = Character('Teacher', color="000000")
# The game starts here.
label start:
"Are you a boy or girl?"
menu:
    "I am a manly MAN": 
        jump intro
    "I am a strong, independent WOMAN":    
        jump intro
label intro:    
    "I can't believe mom and dad made me transfer into high school in the middle of the year, I'd rather be homeschooled!"
    "Why did we have to move! Oh well, I may be able to find someone here to hang out with, since I went to an elementary school in this area."
    "Wandering around the school like a confused sloth, of course I bump into someone."
    m "Oh I'm sorry!"
    "Wait....is that..."
    m "LUCAS!!!! I've missed you so much! "
    "He was my childhoosd friend from elementary school, now I know luck is on my side!"
    l "huh you're....oh gosh...we used to swim in the lake, go hang out at the park..."
    l "Sorry it's been so long, what is your name again? I feel terrible, but I really do remember you."
    $ p = renpy.input("What is your name?") 
    $ p = p.strip()
    if p == "":
        $ p="fuckboy"
    l "Right, Sorry about forgetting. Anyway, would you like to have lunch with me and my friends this afternoon, %(p)s! We have so much to catch up."
menu:
        "Sorry, but no thanks":
            jump sorry
        "Of course! I've missed you so much!":
            jump of
label sorry:
    "After I uttered those words, the air suddenly shifted and became tense."
    l "Oh,um, okay then. I guess I'll see you around? Well, probably not."
    "We never spoke again. In this school I was unable to approach anyone and no one was friendly enough to talk to me."
    "I ended up getting all A's only due to my lack of a social life, but at least my parents are proud."
    "Bad Ending."

    
return

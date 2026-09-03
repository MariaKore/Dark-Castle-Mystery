# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator", kind=narrator) # idk if we need the kind indication 
define y = Character("You")
define dragon = Character("Little Dragon")



# The game starts here.

# Important: files are placeholders, and will get much neater art 

label beginning:

    scene night sky   

    show little dragon

    n "It's night but you can't fall asleep."
    n "You look at the window and stare at the large rocky hill. It has nothing on it but nature and a small cave." # idk whether to add a cave though 
    n "At exactly 12:12 am, a spooky gothic dark castle appears on that hill."
    y "Huh? :0"
    n "Your closest best friend disappeared 12 days ago at exactly 12:12 pm."
    "You had a yummy picnic at the park having a wonderful time with your bestie."
    "They were literally there with you at the picnic table, and poof they disappear!"   

    return

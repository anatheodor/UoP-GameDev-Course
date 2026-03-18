# Defining the characters
define player = Character("[player_name]", color="FFFFFF")
define e = Character("Emma", color="#FFC0CB", image = "emma")
define a = Character("Alex", color="#ADD8E6", image = "alex")
define principal = Character("Principal", color="#DDDDDD")

# Variables to track relationships
default relationship_alex = 0
default relationship_emma = 0

# Character sprites
# Alex
image Alex normal = ("images/Alex normal.png")
image Alex angry = ("images/Alex angry.png")
image Alex happy = ("images/Alex happy.png")
image Alex sad = ("images/Alex sad.png")

#Emma
image Emma normal = ("images/Emma normal.png")
image Emma angry = ("images/Emma angry.png")
image Emma happy = ("images/Emma happy.png")
image Emma sad = ("images/Emma sad.png")

# Blurred background
image bg classroom blurred = im.Blur("images/bg classroom day.png", 5)

# Screen to display relationship "Alex + Emma"
screen relationship_status():
    frame:
        align (0.95, 0.05) # Positioned at the top right
        vbox:
            text "Relationships:"
            text "Alex: [relationship_alex]" color "#87CEEB"
            text "Emma: [relationship_emma]" color "#FFB6C1"

label start:
    scene bg classroom blurred with dissolve

    # Asking for the Player's Name
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() or "Player"

    scene bg classroom day with fade
    play music "audio/main_theme.mp3" loop
    principal "Welcome to the Academy of Arts, [player_name]!"
    principal "We are happy to see you in our school. Here, you'll find not only knowledge but also friends."
    principal "Let me introduce you to our students. They will help you settle in."
    principal "In this game, you must make at least one best friend, or you'll lose..."

    # Go to character introductions
    jump meet_characters

label meet_characters:
    scene bg classroom_2 with dissolve

    # Alex
    show alex normal at center
    a normal "Hi! I'm Alex. If you need help or want to go to the pool, just let me know!"
    a normal "By the way, do you like swimming?"

    menu:
        "Yes, I love it!":
            $ relationship_alex += 1
            a happy "Really? Then you definitely should check out our training session!"
        "Not really. I prefer other types of sports.":
            a sad "Got it. Well, if you ever want to try something new, I'm always here to help."
    hide alex

    scene bg club with dissolve
    # Emma
    show emma normal at center
    e normal "Hello, [player_name]. My name is Emma. I love drawing and reading books."
    e normal "If you want to talk about something interesting, find me in the library."

    menu:
        "I also love reading. Maybe you could recommend something?":
            $ relationship_emma += 1
            e happy "Of course! We have a great collection of books. Come by, and I'll show you."

        "Drawing is awesome. You must be really good at it.":
            $ relationship_emma += 1
            e happy "Thank you! Maybe I'll draw you one day."
    stop music fadeout 2.0
    hide emma 


label first_day:
    scene bg hallway with fade
    show screen relationship_status

    player "The first day at the new academy... I wonder, where should I start?"

    menu:
        "Go to training with Alex.":
            $ relationship_alex += 2
            jump alex_day

        "Visit the library with Emma.":
            $ relationship_emma += 2
            jump emma_day

label alex_day:
    scene bg pool day with dissolve
    play music "audio/pool.mp3" loop
    show alex happy at center

    a happy "I'm happy you came! This is our swimming team's practice session."
    a normal "Let's warm up a bit. Have you swum in a pool before?"

    menu:
        "Of course, I love swimming!":
            $ relationship_alex += 1
            a happy "Cool! Then show me what you got."

        "Not really, but I want to give it a try.":
            a normal "Don't worry, I'll teach you everything you need to know."

    player "Time flew by. Alex is really a great guy."
    stop music fadeout 2.0 
    jump next_day

label emma_day: 
    scene bg library with dissolve 
    play music "audio/library.mp3" loop 
    show emma happy at center 

    e happy "I'm glad you came! This is my favorite library. It's always so peaceful here."
    e normal "What kind of books do you like to read?"

    menu: 
        "I love science fiction and adventure.": 
            $ relationship_emma += 1 
            e happy "Great choice! I love science fiction too. Let me recommend something for you." 
        
        "Historical novels": 
            $ relationship_emma += 1
            e happy "Really? I recently read an amazing novel. I think you'd really like it."

    player "Emma turned out to be an incredibly interesting person to talk to. I definitely want to get to know her better."
    stop music fadeout 2.0 
    jump next_day
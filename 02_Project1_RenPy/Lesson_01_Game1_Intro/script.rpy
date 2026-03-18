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

    return
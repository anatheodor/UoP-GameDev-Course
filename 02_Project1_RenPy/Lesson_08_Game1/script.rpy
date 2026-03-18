# Defining the characters
define player = Character("[player_name]", color="FFFFFF")
define e = Character("Emma", color="#FFC0CB", image = "emma")
define a = Character("Alex", color="#ADD8E6", image = "alex")
define principal = Character("Principal", color="#DDDDDD")
define l = Character("Lily", color="#FF0000", image="lily")

# Variables to track relationships
default relationship_alex = 0
default relationship_emma = 0
default relationship_lily = 0

# Defining Variables for Praise Choices 
define praise_alex = False 
define praise_emma = False

# Sprite Transformations 

transform far_left:
    xalign 0.2 
    yalign 1.0 

transform far_right: 
    xalign 0.8 
    yalign 1.0

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

# Lily
image Lily normal = "images/Lily normal.png"
image Lily angry = "images/Lily angry.png"
image Lily happy = "images/Lily happy.png"
image Lily sad = "images/Lily sad.png"

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

# Screen to display relationship "Alex + Emma + Lily"
screen relationship_status2():
    frame:
        align (0.95, 0.05) # Positioned at the top right
        vbox:
            text "Relationships:"
            text "Alex: [relationship_alex]" color "#87CEEB"
            text "Emma: [relationship_emma]" color "#FFB6C1"
            text "Lily: [relationship_lily]" color "#FF0000"

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


label next_day:
    scene bg schoolyard day with fade
    play music "audio/traffic_noise.mp3" loop 
    play sound "audio/argument.mp3" loop 
    player "Today, I decided to take a walk around the school yard. It looks like someone is arguing over there..."

    show alex normal at far_left 
    show emma normal at far_right 

    a angry "I told you that the training was more important than your library meeting!" with hpunch 
    e angry "But I think we shouldn't force everyone to go to the pool! Everyone has their own interests." with hpunch

    player "It looks like I'll have to step in..."

    menu: 
        "Support Alex.": 
            $ relationship_alex += 2
            $ relationship_emma -= 1

            a normal "Thank for the support. I knew you'd understand me."
            e sad "Well, if that's the case, maybe we don't have much more to talk about..."

        "Support Emma.":
            $ relationship_emma += 2
            $ relationship_alex -= 1

            e normal "Thank you! Finally, someone understands me."
            a sad "I thought we were friends. Looks I was wrong."

        "To try to reconcile them.":
            $ relationship_alex += 1
            $ relationship_emma += 1

            a normal "Maybe you're right. We both went a bit too far."
            e normal "Alright, I admit we could have found a compromise. Thanks for your help."

    hide alex 
    hide emma 

    player "It seems like they've calmed down a bit, but we'll see what happens next."
    stop music fadeout 2.0 
    stop sound fadeout 2.0 

label evening_choice: 
    scene bg hallway evening with fade 
    player "Evening at the academy. Everyone has gone off to their own activities, but I decided to take a little walk."
    player "Such open space and peace around..." 
    play sound "audio/room_noise.mp3" 
    player "It seems like there's a sound coming from around the corner... Is it Alex? Or Emma?" with hpunch 

    menu: 
        "Approach Alex.": 
            $ relationship_alex += 1 
            jump alex_secret 

        "Approach Emma.": 
            $ relationship_emma += 1 
            jump emma_secret 

label alex_secret: 
    scene bg pool night spotlight with dissolve 
    play music "audio/pool.mp3" loop 
    play music "audio/cricket1.mp3" loop 
    
    show alex normal at center 

    player "Alex? Are you here alone?"
    a normal "Yeah... Sometimes I come here at night. This place reminds me of the past."
    a sad "I used to be the captain of a team in another city, but we lost the final competition."
    a normal "It was my failure. Since then, I've been training even harder so I never let the team down again."

    menu:
        "Support Alex.":
            $ praise_alex = True 
            $ renpy.notify("Alex will remember that!")
            $ relationship_alex += 3 
            a happy "Thank you... I didn't expect anyone to care."

        "Change the subject.":
            a normal "You're right. Let's talk about something nice."
    player "This night has brought us closer together. I understand Alex better now."
    hide alex 
    jump meet_lily 
    stop music fadeout 2.0 

label emma_secret:
    scene bg art club night spotlight with dissolve 
    play music "audio/drawing.mp3" loop 
    play sound "audio/cricket2.mp3"

    show emma normal at center 

    player "Emma? Are you looking for something?" 
    e "Yeah, I'm working on my new project. I want to create a series of illustrations for our academy."
    e "Drawing is not just a hobby for me. It helps me to forget my difficulties."
    e "I used to hide behind my drawings a lot when I felt lonely."

    menu:
        "Praise her talent.":
            $ praise_emma = True
            $ renpy.notify("Emma will remember that!")
            $ relationship_emma += 3
            e happy "Thank you! Do you really think I can do this?"

        "Share your feelings.":
            e normal "This is so unexpected. But I guess I can trust you, too."

    player "This evening helped me realize how deep a person Emma is."
    stop music fadeout 2.0 
    stop sound fadeout 2.0 
    hide emma 

label meet_lily:
    scene bg schoolyard day with fade
    play music "audio/traffic_noise.mp3" loop 
    show screen relationship_status2

    player "This afternoon I decided to take a walk in the academy courtyard. There are always a lot of interesting people here..."
    play sound "audio/heels.mp3"
    $ renpy.pause(5)
    player "Wait, who's that? I don't think I've ever seen her before."
    stop sound
    play sound "audio/colliding.mp3"
    show lily normal at center with hpunch
    l "You seem new. I'm surprised we haven't met before."
    player "Hi. Who are you?"
    l "Lily. Just Lily. And I hear you're already friends with Alex and Emma?"
    player "How do you know?"
    l "I know a lot. Maybe even more than they want to tell you."

    menu:
        "Try to learn more about her.":
            $ relationship_lily += 2
            l "Curiousity is a good trait. But it's not always safe."

        "Stay alert.":
            l "You don't want to talk? Well, then just watch. Sometimes it's even more interesting."

    player "Lily left me with a strange feeling. I definitely want to understand her better."
    stop music fadeout 2.0 

label classroom_argument:
    scene bg classroom day with fade 
    play sound "audio/classroom_noise.mp3" loop 
    player "Today all three of them - Alex, Emma and Lily - are gathered in the classroom. The atmosphere is tense."

    show alex angry at far_left with vpunch 
    show emma normal at center with vpunch 
    show lily normal at far_right with vpunch 

    a angry "Why do you always interfere, Lily? It's none of your business!"
    e normal "Alex, stop! Lily's just trying to help..."
    l happy "Come on, let's not fight. I was just trying to come up with an interesting solution."

    menu:
        "Support Alex.":
            $ relationship_alex += 2
            $ relationship_emma -= 1
            $ relationship_lily -= 1 
            a happy "Thank you for being on my side. I knew I could count on you."
            l "How predictable."

        "Support Emma.":
            $ relationship_emma += 2
            $ relationship_alex -= 1
            $ relationship_lily += 1
            e happy "Thank you. I knew you understood me."
            a sad "How on earth can you cross over so easily?"

        "Support Lily.":
            $ relationship_lily += 2
            $ relationship_alex -= 1
            $ relationship_emma -= 1
            l happy "Interesting choice. I knew you were a smart man."
            e angry "Do you really believe her? She's just playing with us!"

    stop music fadeout 2.0 
    player "This choice will definitely affect our relationship..."

label lily_secret:
    scene bg hallway night with fade
    play sound "audio/cricket2.mp3" loop 
    player "Night has fallen." 
    player "The academy had gone completely dark." 
    scene bg club night with fade 
    player "But I think there's someone in the library."
    player "Let's see..." 
    scene bg library night spotlight with fade 
    show lily normal at center with hpunch 
    player "It's Lily. But what is she doing out at this hour?"
    show lily angry at center 
    play sound "audio/sigh.mp3"

    l angry "Are you watching me? You have a good nose for secrets..." with hpunch
    player "I was just wondering why you're here at night."
    l angry "Why? Sometimes I'm looking for answers to questions that others aren't interested in."
    l normal "For example, how to use information about people to achieve your goals."

    menu: 
        "Wonder and try to understand her.":
            $ relationship_lily += 2
            l happy "I knew you'd understand. You and I are alike, in a way."
            jump mini_game_cipher

        "Condemn her for manipulation.":
            $ relationship_lily -= 2
            l angry "Hmm, what a boring response. Maybe you're not as interesting as I thought you were."
    stop sound fadeout 2.0 
    player "After that conversation, I began to look at Lily very differently."
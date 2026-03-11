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
image Alex normal = ("images/Sprites/Alex normal.png")
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
    principal "Welcome to the Performing and Digital Arts Department, [player_name]!"
    principal "We are happy to see you at University of the Peloponnese. Here, you'll find not only knowledge but also friends."
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
            e happy "Of course! We have a great collection of books at Aria building. Come by, and I'll show you."

        "Drawing is awesome. You must be really good at it.":
            $ relationship_emma += 1
            e happy "Thank you! Maybe I'll draw you one day."

    stop music fadeout 2.0
    hide emma 

label first_day:
    scene bg hallway with fade
    show screen relationship_status

    player "The first day at the new university... I wonder, where should I start?"

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
    player "Today, I decided to take a walk around the univeristy yard. It looks like someone is arguing over there..."

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

transform half_size:
    zoom 0.5 # Downsizing by up to 50%
    xalign 0.5 # Horizontal centering
    yalign 0.5 # Verticsl centering

label mini_game_cipher:
    scene bg library night with fade
    play sound "letter_opening.mp3"
    show cipher at half_size with fade
    play sound "audio/strange.mp3"

    player "I found a strange letter on the table. I think it's encrypted..."

    $ cipher_text = "Zpv bsf tpnfpoft dvsjpvt." # You are someone's curious. (Shifted)
    $ correct_answer = "you are someone's curious."
    $ player_answer = ""
    $ attempts = 3

    while attempts > 0:
        menu:
            "Try to decipher the text":
                $ renpy.notify("Try shifting one letter back in the alphabet.")
                $ player_answer = renpy.input(f"Letter: {cipher_text}")
                $ player_answer = player_answer.strip().lower() # Remove spaces and convert to lowercase

                if player_answer == correct_answer:
                    jump cipher_success
                else:
                    $ attempts -= 1
                    if attempts > 0:
                        "Incorrect. Attempts left: [attempts]."
                    else:
                        jump cipher_fail
            "Give up trying":
                jump cipher_fail

label cipher_success:
    play sound "audio/success.mp3"
    show screen transparent_window_success
    show success at truecenter with dissolve

    player "I was able to decipher the letter! What did it say?"

    $ relationship_lily += 3

    hide screen transparent_window_success with dissolve
    hide success with dissolve

    player "It says: You are someone's curious."

    jump lily_vs_others
    return

label cipher_fail:
    play sound "audio/fail.mp3"
    show screen transparent_window_fail
    show fail at truecenter with dissolve

    player "I was not able to decipher the letter. I wonder what was in it?"

    $ relationship_lily -= 3

    hide screen transparent_window_fail with dissolve
    hide fail with dissolve
    return


label lily_vs_others:
    scene bg schoolyard day with fade
    play music "audio/traffic_noise.mp3" loop 
    play sound "audio/argument.mp3" loop 
    player "It's a new day."
    player "I walked up to the group when I saw Lily explaining something to Alex and Emma."

    show alex angry at far_left with fade 
    show emma sad at center with fade 
    show lily happy at far_right with fade

    a angry "You can't do this to people! It's not right." with hpunch 
    e angry "I, too, think you're going too far." with hpunch 
    l happy "Relax, I'm just helping you understand how the world works. If you can't see it, that's your problem."

    menu:
        "Support Lily.":
            $ relationship_lily += 2
            $ relationship_alex -= 1
            $ relationship_emma -= 1

            l happy "Finally someone sees things for what they are. You didn't dissapoint me."

        "Take Alex and Emma's side.":
            $ relationship_lily -= 2
            $ relationship_alex += 1
            $ relationship_emma += 1

            a happy "Thank you. I guess you understand what true friendship is."
            e happy "I'm glad you're with us. Together, we're gonna take care of Lily."

        "Try to resolve the conflict.":
            $ relationship_lily += 1
            $ relationship_alex += 1
            $ relationship_emma += 1

            l happy "What a peacemaker you are. That's commendable, but sometimes it doesn't work."
            a normal "Maybe you're right. Lily's not gonna change anyway."
            e sad "I hope you know what you're doing."

    player "Things have gotten heated. Looks like we're gonna have to make a choice..."

    stop music fadeout 2.0
    stop sound fadeout 2.0
    jump determine_ending


label lily_ending:
    play music "audio/comedy.mp3" loop 
    scene bg schoolyard day with fade 
    show lily happy at center 

    l happy "I'm glad you stayed with me to the end. Very few people realize that you have to fight for your ambitions."
    l normal "Together we can acomplish anything we want. What do you say?"

    menu:
        "To agree and become her partner.":
            play sound "audio/woman_laugh.mp3"
            $ relationship_lily += 5
            l happy "I knew you'd make the right choice. We'll get through this."
            player "Lily's ambitious ending."
            jump end_game

        "Give up and go your own way.":
            play sound "glass_breaking.mp3"
            $ relationship_lily -= 5 
            l sad "I thought you were different. I'm sorry I was wrong."
            player "Breaking ties with Lily."
            jump end_game

label alex_ending:
    scene bg pool day with fade
    play music "audio/friendly.mp3" loop 
    play audio "audio/pool.mp3" loop 
    show alex happy at center 

    a normal "I have a crucial competition today, and I want you by my side."

    if praise_alex:
        a happy "I remember how you supported me in a difficult moment. It helped me to believe in my abilities and I decided to participate."
    
    menu:
        "Support Alex in the competition.":
            $ relationship_alex += 5
            show confetti behind alex 
            a happy "With your support, I was able to do it. Now I know that anything is possible."
            a happy "Thank you for everything. You are a special person and I want you to always be there for me."
            player "Romantic ending with Alex."
            stop audio fadeout 2.0
            jump end_game
        
        "Refuse and stand aside.":
            $ relationship_alex -= 3
            a sad "I wish you could share this moment with me."
            a normal "But I'm still grateful for what you've done for me."
            player "Friendly ending with Alex."
            stop audio fadeout 2.0
            jump end_game

label emma_ending:
    play music "audio/main_theme.mp3" loop 
    scene bg art club day with fade 
    show emma happy at center 

    e happy "I am thankful for everything, your support has helped me achieve this."
    e happy "My first exhibition is just the beginning, but I never would have decided to do it without your help."

    if praise_emma:
        e happy "I remember when you praised me. It helped me believe in my talent."
    
    menu:
        "Confess your feelings.":
            $ relationship_emma += 5
            show confetti behind emma 
            e happy "You've always been there for me and understood me like no one else. I'm happy you're here."
            player "Romantic ending with Emma."
            jump end_game
        
        "Congratulate and stay friends.":
            $ relationship_emma -= 2
            e normal "You're my best friend, and I'll never forget that."
            player "Friendly ending with Emma."
            jump end_game

label dramatic_ending:
    play sound "audio/fail_trumpet.mp3"
    scene bg classroom day with fade
    player "I ended up alone. No one wanted to stay with me."
    player "Sometimes the choices we make come with a price, and I realized that too late."
    player "Bad ending."
    jump end_game
    return

label determine_ending:
    if relationship_alex > relationship_emma and relationship_alex > relationship_lily:
        jump alex_ending
    elif relationship_emma > relationship_alex and relationship_emma > relationship_lily:
        jump emma_ending
    elif relationship_lily > relationship_alex and relationship_lily > relationship_emma:
        jump lily_ending
    else:
        jump dramatic_ending
    return

label end_game:
    # Show Black Background
    show screen end_screen
    # Delay Before Exiting to the Main Menu or Ending the Game
    pause 3
    # $ renpy.pause(3)
    # Back to Main Menu
    return    

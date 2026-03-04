# Αρχικοποίηση χαρακτήρων σε μεταβλητές
# Η παράμετρος color αλλάζει το χρώμα στο label του κάθε χαρακτήρα σε τιμή Hex Code #RRGGBB
define e = Character("Eileen", color = "#FF0000")
define t = Character("Teileen", color = "#0000FF")

# Κάνουμε scale τις εικόνες που χρησιμοποιούμε (είτε χαρακτήρων είτε bg)
# Όσον αφορά τα bg ανάλογα με την αρχική μας επιλογή ανάλυσης π.χ., 1920x1080
# Προσοχή στα πεζά/κεφαλαία και στο σωστό path - επέκταση του αρχείου εικόνας
image b = im.Scale("images/bear.png", 634, 1000)
image r = im.Scale("images/room.png", 1920, 1080)

# Με ετικέτες-labels χωρίζουμε τις ενότητες του έργου
# Προσοχή στις εσοχές!! Δεν τις πειράζουμε
label start:
    # εμφάνιση του bg με όνομα μεταβλητής r
    scene r
    
    # εμφάνιση του χαρακτήρα με όνομα μεταβλητής b
    # Δείτε και https://www.renpy.org/doc/html/transitions.html
    show b

    # Displaying Images link: https://www.renpy.org/doc/html/displaying_images.html
    show b with dissolve:
        xalign 0.0
        yalign 0.0

    pause

    # ήχος, προσοχή στην παρακάτω εντολή το αρχείο ήχου είναι στην τοποθεσία root (στο φάκελο audio)
    play music "act.wav"
    # το παρακάτω θα παίξει μόνο 1 φορά
    # play sound "act.wav"

    # Διάλογος του e
    e "You've created a new Ren'Py game. How are you?"
    
    # Διάλογος του t
    t "I'm good, have your first choice now!"

    # τέλος ήχου
    stop music fadeout 4

    # Δημιουργία επιλογών, τα jump είναι η συνέχεια της ιστορίας
    # Προσοχή στις εσοχές
    menu:
        "Choose path 1":
            # Η εντολή jump πάει στο αντίστοιχο label και συνεχίζει από εκεί
            # Υπάρχει και η εντολή call, που καλεί το αντίστοιχο label και μετά συνεχίζει από εδώ
            jump path1
        "Choose path 2":
            jump path2


# Οι ετικέτες ξεκινούν με αριστερή στοίχιση (χωρίς εσοχή)
label path1:
    e "You're in path 1"
    # Η εντολή return τερματίζει το παιχνίδι και επιστρέφει στο Main Menu
    return

label path2:
    e "You're in path 2"

    # μεταβλητή boolean που μπορώ να χρησιμοποιήσω για να επιλέξω ανάμεσα από επιλογές
    # εδώ αρχικοποιείται ως true (ΚΩΔΙΚΑΣ PYTHON)
    $ learned = True
    
    jump choices


label choices:
    # δομή επιλογής (Conditional Logic)
    if learned:
        e "I am true!!"
    else:
        e "I am false :)"

    # Η επιστροφή στο μενού, έξω από την if/else
    return

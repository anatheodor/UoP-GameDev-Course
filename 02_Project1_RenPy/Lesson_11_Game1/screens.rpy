### Place this code at the bottom of your screens.rpy file

### End of the Game
screen end_screen():
    zorder 100
    modal True

    frame:
        background "#000000"
        xfill True
        yfill True 

    text "End of Game":
        color "#FFFFFF"
        size 100
        xalign 0.5
        yalign 0.5
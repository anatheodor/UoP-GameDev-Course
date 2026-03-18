### Place this code at the bottom of your screens.rpy file

### Cipher Game Success
screen transparent_window_success:
    window:
        xysize (1920, 1080) # Window size
        yoffset 0 # Vertical offset
        background "#00FF00AA" # Semi-transparent green background

### Cipher Game Fail
screen transparent_window_fail:
    window:
        xysize (1920, 1080) # Window size
        yoffset 0 # Vertical offset
        background "#FF0000AA" # Semi-transparent red background
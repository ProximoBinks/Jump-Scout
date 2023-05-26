import keyboard
import time
import winsound
import threading

# Constants
DELAY = 0.35467896461488#0.40467896461488  # Delay in seconds before playing the beep sound
DURATION = 200  # Duration of the beep sound in milliseconds

# Variable
last_space_press_time = 0

# Function to play the beep sound
def play_beep():
    winsound.Beep(440, DURATION)  # Frequency: 440Hz, Duration: DURATION ms

# Function to handle Spacebar key events
def on_space_event(event):
    global last_space_press_time
    if event.name == 'space' and event.event_type == 'down':
        current_time = time.time()
        if current_time - last_space_press_time >= DELAY:
            last_space_press_time = current_time
            # Create a thread to play the beep sound after the delay
            threading.Timer(DELAY, play_beep).start()

# Register the callback function for key events
keyboard.on_press(on_space_event)

# Keep the script running until 'Esc' key is pressed
keyboard.wait('esc')

# Unregister the callback function
keyboard.unhook_all()  
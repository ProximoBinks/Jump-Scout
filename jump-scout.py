import csv
import keyboard
import time

# Variables
keystrokes = []
start_time = time.time()

# Function to handle keystroke events
def on_key_event(event):
    keystrokes.append((event.name, time.time() - start_time))

# Register the callback function for key events
keyboard.on_press(on_key_event)

# Wait for 20 seconds
time.sleep(20)

# Unregister the callback function
keyboard.unhook_all()

# Export keystrokes to a CSV file
with open('keystrokes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key', 'Time'])
    writer.writerows(keystrokes)

print("Keystrokes recorded and exported to keystrokes.csv")

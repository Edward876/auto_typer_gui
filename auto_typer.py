import pyautogui
import tkinter as tk
import pyperclip
from pynput import keyboard
import threading

# Global variable to track whether typing is in progress
typing_in_progress = False

def auto_typer(wpm):
    global typing_in_progress

    # For extremely high WPM, type everything instantly
    if wpm >= 10000:
        text = pyperclip.paste()  # Get text from clipboard
        pyautogui.write(text)  # Write entire text instantly
    else:
        # Calculate delay between each character based on WPM (1 word = 5 characters)
        delay = 60 / (wpm * 5)
        text = pyperclip.paste()

        # Start typing each character with delay
        for char in text:
            if not typing_in_progress:
                break
            pyautogui.typewrite(char)
            time.sleep(delay)

def on_press(key):
    global typing_in_progress

    try:
        # Get the selected start/stop key from the entry
        selected_key = key_entry.get().lower()

        # Check if the pressed key matches the selected key
        if key == keyboard.Key[selected_key]:
            if typing_in_progress:
                # Stop typing if it's already in progress
                typing_in_progress = False
            else:
                # Start typing if it's not in progress
                typing_in_progress = True
                wpm = float(wpm_entry.get())
                threading.Thread(target=auto_typer, args=(wpm,), daemon=True).start()
    except AttributeError:
        pass

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.daemon = True  # Make listener run in the background
    listener.start()

def start_typing():
    text = text_entry.get()
    pyperclip.copy(text)  # Copy the text to clipboard
    threading.Thread(target=start_listener, daemon=True).start()

# Creating the GUI
app = tk.Tk()
app.title("Auto Typer App")
app.geometry("400x400")  # Set the window size

# Text input field
tk.Label(app, text="Text to Type:").pack(pady=5)
text_entry = tk.Entry(app, width=50)
text_entry.pack(pady=5)

# WPM input field
tk.Label(app, text="Words Per Minute (WPM):").pack(pady=5)
wpm_entry = tk.Entry(app, width=10)
wpm_entry.pack(pady=5)
wpm_entry.insert(0, "60")  # Default to 60 WPM

# Key input field
tk.Label(app, text="Start/Stop Key (e.g., 'f1', 'f2'):").pack(pady=5)
key_entry = tk.Entry(app, width=10)
key_entry.pack(pady=5)
key_entry.insert(0, "f2")  # Default to F2

# Start button
start_button = tk.Button(app, text="Start Typing", command=start_typing)
start_button.pack(pady=20)

# Footer label with creator's name
footer_label = tk.Label(app, text="Made by Shilly Joestar", font=("Helvetica", 8, "italic"), fg="gray")
footer_label.pack(side="bottom", pady=10)

# Run the app
app.mainloop()

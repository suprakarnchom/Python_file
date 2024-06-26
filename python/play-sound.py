import tkinter as tk
from tkinter import messagebox
import pygame

# Function to be called when the button is clicked
# def on_button_click():
#     messagebox.showinfo("Information", "Button Clicked!")

# Function to be called when the button is clicked
def on_button_click():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/chompu/Documents/Meta Back end/media/f6-note.flac")
    pygame.mixer.music.play()

def on_second_button_click():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/chompu/Documents/Meta Back end/media/g5-note.flac")
    pygame.mixer.music.play()


def on_third_button_click():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/chompu/Documents/Meta Back end/media/lbrazo-003.wav")
    pygame.mixer.music.play()


# Create the main window
root = tk.Tk()
root.title("Playsound GUI")

# Create a label widget
label = tk.Label(root, text="Hello, Musician!")
label.pack(pady=10)


# Create the first button widget
button1 = tk.Button(root, text="Play F6", command=on_button_click)
button1.pack(pady=10)

# Create the second button widget
button2 = tk.Button(root, text="Play G6", command=on_second_button_click)
button2.pack(pady=10)

# Create the third button widget
button3 = tk.Button(root, text="Play Lbrazo", command=on_third_button_click)
button3.pack(pady=10)

# Create the quit button widget
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)



# Run the application
root.mainloop()


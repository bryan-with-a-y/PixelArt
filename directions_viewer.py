# KeyLogger_tk2.py
# show a character key when pressed without using Enter key
# hide the Tkinter GUI window, only console shows
import os, sys
import subprocess
from posixpath import join

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def show_region():
    while True:
        region = input("Enter x and y of desired region: ")
        x,y = region.strip().split(" ")
        region = "X-{}_Y-{}".format(x,y)
        region_dir = "C:/Users/김태양/Documents/programming/ColorWorker/projects/coufal_present/directions/block/{}/".format(region)
        images = os.listdir(region_dir)
        for image_name in images:
            image_fp = join(region_dir, image_name)
            command = "explorer {}".format(image_fp)
            print(command)
            process = subprocess.Popen(['explorer', image_fp],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
            return
def key(event):
    """shows key or tk code for the key"""
    pressed_key = event.keysym
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:
        # normal number and letter characters
        if pressed_key == "j":
            region = input("Enter x and y of desired region")
            #print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        if pressed_key == "Left":
            X -= 1
        elif pressed_key == "Right":
            X += 1
        elif pressed_key == "Up":
            Y -= 1
        elif pressed_key == "Down":
            Y += 1
        #print( 'Special Key %r' % event.keysym )
    x,y = region.strip().split(" ")
    show_region(x,y)


def main():
    show_region()

main()
"""
root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()"""

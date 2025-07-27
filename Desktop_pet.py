import tkinter as tk
import time
import random

class pet():
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        # placeholder image
        self.walking_right = [tk.PhotoImage(file='walking_right.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        self.timestamp = time.time()

        self.window.config(highlightbackground='black')

        self.window.overrideredirect(True)

        self.window.attributes('-topmost', True)

        self.window.wm_attributes('-transparentcolor', 'black')

        self.label = tk.Label(self.window, bd=0, bg='black')

        self.x = 0
        self.window.geometry('64x64+{x}+0'.format(x=str(self.x)))

        self.label.configure(image=self.img)

        self.label.pack()

        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        self.x += 1

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.walking_right[self.frame_index]

        # create the window
        self.window.geometry('64x64+{x}+0'.format(x=str(self.x)))
        self.label.configure(image=self.img)
        self.label.pack()

        self.window.after(10, self.update)

pet()
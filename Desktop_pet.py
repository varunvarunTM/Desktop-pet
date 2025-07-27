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
        self.y = 0  # Add y coordinate
        self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))

        self.label.configure(image=self.img)
        self.label.pack()

        # ADD DRAG FUNCTIONALITY:
        self.dragging = False
        self.start_x = 0
        self.start_y = 0
        
        # Bind mouse events to the label
        self.label.bind("<Button-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<ButtonRelease-1>", self.stop_drag)

        self.window.after(0, self.update)
        self.window.mainloop()

    def start_drag(self, event):
        """Called when mouse button is pressed"""
        self.dragging = True
        self.start_x = event.x_root - self.window.winfo_x()
        self.start_y = event.y_root - self.window.winfo_y()

    def on_drag(self, event):
        """Called when mouse is moved while button is held"""
        if self.dragging:
            new_x = event.x_root - self.start_x
            new_y = event.y_root - self.start_y
            self.x = new_x
            self.y = new_y
            self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))

    def stop_drag(self, event):
        """Called when mouse button is released"""
        self.dragging = False

    def update(self):
        # Only move automatically if not being dragged
        if not self.dragging:
            self.x += 1

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.walking_right[self.frame_index]

        # Update window position only if not dragging
        if not self.dragging:
            self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        
        self.label.configure(image=self.img)
        self.label.pack()

        self.window.after(10, self.update)


pet()


# This class draws an arc on a canvas using the tkinter library

import tkinter

class DrawArc:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.create_arc(10, 10, 190, 190, start = 45, extent = 30)
        self.canvas.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    MyArc = DrawArc()
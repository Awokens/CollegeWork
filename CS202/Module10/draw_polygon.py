
# This class draws a polygon on a canvas using the tkinter library

import tkinter

class DrawPolygon:
    def __init__(self):
        self.main_window
        self.canvas = tkinter.Canvas(self.main_window, width = 160, height = 160)
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60)
        self.canvas.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    MyPolygon = DrawPolygon()
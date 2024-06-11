
# This class draws text in an open canvas using the tkinter library

import tkinter

class DrawText:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        self.canvas.create_text()
        self.canvas.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    MyCanvas = DrawText()

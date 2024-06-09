
import tkinter as tk

def createSolarSystem(canvas):

    canvas.create_oval(600, 300, 700, 300, fill = 'yellow')
    canvas.create_text(600, 400, text = 'sun', fill = 'white')

    planets = [(100, 3, 'gray', 'Mercury'),
        (125, 5, 'orange', 'Venus'),
        (175, 6, 'blue', 'Earth'),
        (250, 10, 'brown', 'Jupiter'),
        (350, 8, 'yellow', 'Saturn'),
        (400, 7, 'light blue', 'Uranus'),
        (450, 7, 'blue', 'Neptune'),
        (500, 2, 'light blue', 'Pluto')]
    
    for distance, radius, color, name in planets:
        y = 200
        x = 400 + distance
        canvas.create_text(x, y + radius + 20, text = name, fill = 'white')
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = color)
        

def main():
    instance = tk.Tk()
    instance.title('Our Solar System')

    canvas = tk.Canvas(root, width = 1280, height = 720, bg = 'black')
    canvas.pack()
    createSolarSystem(canvas)
    instance.mainloop()

if __name__ == '__main__':
    main()
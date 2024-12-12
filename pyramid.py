import tkinter

def change_color(canvas, color):
    """Change the background color of the canvas."""
    canvas.config(bg=color)

# Set up the window
window = tkinter.Tk()
window.title("Change Background Color")

# Set up the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
canvas = tkinter.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Create buttons to change the color
button_red = tkinter.Button(window, text="Red", command=lambda: change_color(canvas, "red"))
button_red.pack(side=tkinter.LEFT, padx=10, pady=10)

button_green = tkinter.Button(window, text="Green", command=lambda: change_color(canvas, "green"))
button_green.pack(side=tkinter.LEFT, padx=10, pady=10)

button_blue = tkinter.Button(window, text="Blue", command=lambda: change_color(canvas, "blue"))
button_blue.pack(side=tkinter.LEFT, padx=10, pady=10)

# Run the tkinter event loop
window.mainloop()

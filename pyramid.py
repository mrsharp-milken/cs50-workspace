import tkinter

def draw_rectangle(canvas, width):
    """Draw a rectangle with the specified width centered on the canvas."""
    # Convert width input to an integer
    width = int(width)

    # Clear the canvas
    canvas.delete("all")

    # Rectangle dimensions
    height = 50  # Fixed height
    x1 = (CANVAS_WIDTH - width) // 2
    y1 = (CANVAS_HEIGHT - height) // 2
    x2 = x1 + width
    y2 = y1 + height

    # Draw the rectangle
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")

# Set up the window
window = tkinter.Tk()
window.title("Draw a Rectangle")

# Canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
canvas = tkinter.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Prompt for user input
width_input = input("Enter rectangle width: ")

# Draw the rectangle
draw_rectangle(canvas, width_input)

# Run the tkinter event loop
window.mainloop()

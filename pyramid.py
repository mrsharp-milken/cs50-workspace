import tkinter

def draw_rectangle(canvas, width):
    """Draw a rectangle with the specified width centered on the canvas."""
    try:
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
    except ValueError:
        # Handle invalid input
        result_label.config(text="Please enter a valid number.")

# Set up the window
window = tkinter.Tk()
window.title("Draw a Rectangle")

# Canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
canvas = tkinter.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Entry widget for input
entry_label = tkinter.Label(window, text="Enter rectangle width:")
entry_label.pack()
width_entry = tkinter.Entry(window)
width_entry.pack()

# Button to draw the rectangle
draw_button = tkinter.Button(window, text="Draw Rectangle",
                              command=lambda: draw_rectangle(canvas, width_entry.get()))
draw_button.pack()

# Label to show feedback
result_label = tkinter.Label(window, text="")
result_label.pack()

# Run the tkinter event loop
window.mainloop()

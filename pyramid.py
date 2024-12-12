"""
File: pyramid.py
----------------
ADD YOUR DESCRIPTION HERE
"""


import tkinter
from tkinter import simpledialog

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels


def draw_rectangle(canvas):
    """Draw a rectangle with the specified width centered on the canvas."""

    width = simpledialog.askstring("Rectangle", "Enter rectangle width:")
    width = int(width)

    # Rectangle dimensions
    height = 50  # Fixed height
    x1 = (CANVAS_WIDTH - width) // 2
    y1 = (CANVAS_HEIGHT - height) // 2
    x2 = x1 + width
    y2 = y1 + height

    # Draw the rectangle
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")



######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('Circle')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_rectangle(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()

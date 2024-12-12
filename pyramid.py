"""
File: pyramid.py
----------------
ADD YOUR DESCRIPTION HERE
"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_pyramid(canvas):
    """
    ADD YOUR COMMENT
    """
    for row in range(BRICKS_IN_BASE):
        # Calculate the number of bricks in the current row
        bricks_in_row = BRICKS_IN_BASE - row

        # Calculate the horizontal starting position for the first brick
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) // 2

        # Calculate the vertical position for the row
        start_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        for brick in range(bricks_in_row):
            # Calculate the position of each brick
            x1 = start_x + brick * BRICK_WIDTH
            y1 = start_y
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT

            # Draw the brick as a rectangle
            canvas.create_rectangle(x1, y1, x2, y2)


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
    top.title('pyramid')
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
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
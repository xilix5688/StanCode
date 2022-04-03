"""
File: draw_line
Name: 游雅媛
-------------------------
TODO: This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

SIZE = 5

window = GWindow()
pen_stroke_x = 0
pen_stroke_y = 0
pen_stroke = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle)


def circle(event):
    global pen_stroke_x, pen_stroke_y
    window.add(pen_stroke, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
    pen_stroke_x = event.x
    pen_stroke_y = event.y

    onmouseclicked(line)


def line(event2):
    global pen_stroke_x, pen_stroke_y

    window.remove(pen_stroke)
    draw_line = GLine(pen_stroke_x, pen_stroke_y, event2.x, event2.y)
    window.add(draw_line)

    onmouseclicked(circle)


if __name__ == "__main__":
    main()

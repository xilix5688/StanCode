"""
This program simulates a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
LIVES = 3

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0


def set_ball():
    """
    To set up the ball to the original position.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    set_ball()
    onmouseclicked(bouncing)


def bouncing(event):
    global count
    vy = 0

    if count <= LIVES:
        while ball.x < 800:
            if ball.y > 500 and vy > 0:
                vy = -vy * REDUCE

            vy += GRAVITY
            ball.move(VX, vy)
            pause(DELAY)

        count += 1
        set_ball()


if __name__ == "__main__":
    main()

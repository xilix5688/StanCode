"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The program plays a Python game that a user has to control the paddle to keep the ball bouncing and
breaking all the bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()

    while True:
        speed_x = graphics.get_dx()
        speed_y = graphics.get_dy()
        graphics.ball.move(speed_x, speed_y)
        pause(FRAME_RATE)
        graphics.collision_bounce()
        graphics.restart()







if __name__ == '__main__':
    main()

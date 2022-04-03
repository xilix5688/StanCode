"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.count_failed = 0  # 球超出底部次數

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.window.add(self.paddle, x=(self.window_width - paddle_width) / 2, y=(self.window_height - paddle_height - paddle_offset))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)
        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

        # Draw bricks
        w = 0  # width
        offset = brick_offset
        for i in range(brick_rows):
            offset += brick_height + brick_spacing
            for j in range(brick_cols):
                w = j*(brick_width + brick_spacing)
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if i // 2 == 0:
                    brick.fill_color = 'red'
                elif i // 2 == 1:
                    brick.fill_color = 'orange'
                elif i // 2 == 2:
                    brick.fill_color = 'yellow'
                elif i // 2 == 3:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick, w, offset)

        self.original_x = self.window_width / 2 - ball_radius
        self.original_y = self.window_height / 2 - ball_radius

    def paddle_move(self, mouse):
        if mouse.x > self.window_width:
            self.paddle.x = self.window_width - self.paddle_width
        else:
            self.paddle.x = mouse.x - self.paddle_width / 2
            self.paddle.y = self.window_height - self.paddle_height - self.paddle_offset

    def start(self, mouse):
        if self.original_x == self.ball.x and self.original_y == self.ball.y:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if (random.random() > 0.5):
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_ball(self):
        return self.ball

    def collision_bounce(self):
        if self.ball.x <= 0 or self.ball.x + 2 * BALL_RADIUS >= self.window_width:  # 碰到左右邊界反彈
            self.__dx = -self.__dx
        if self.ball.y <= 0:  # 碰到邊界反彈
            self.__dy = -self.__dy
        if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1) is not None and \
                self.ball.y + 2*BALL_RADIUS + 1 >= self.paddle.y:  # 碰到板子
            self.__dy = -self.__dy
        else:
            if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1))
                self.__dy = -self.__dy
            if self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS))
                self.__dx = -self.__dx
            if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS+1, self.ball.y + 2 * BALL_RADIUS+1))
                self.__dy = -self.__dy
            if self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS + 1, self.ball.y + BALL_RADIUS) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS +1, self.ball.y + BALL_RADIUS))
                self.__dx = -self.__dx

    def restart(self):
        if self.ball.y > self.window_height:
            if self.count_failed == 2:
                self.window.remove(self.ball)
            else:
                self.window.add(self.ball, x=self.window_width / 2 - BALL_RADIUS, y=self.window_height / 2 - BALL_RADIUS)
                self.count_failed += 1













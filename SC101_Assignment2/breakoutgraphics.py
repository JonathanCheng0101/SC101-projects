"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
Name:jonathan cheng

"""

"""
file:breakout.py
name:jonathan cheng
"""
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmousemoved, onmouseclicked
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
FRAME_RATE = 1000 / 120
lives=3

class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle = GRect(paddle_width,paddle_height)   # Create a paddle.
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.window.add(self.paddle,(self.window.width-paddle_width)/2, self.window.height-PADDLE_OFFSET)
        self.ball = GOval(ball_radius,ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "darkred"
        self.window.add(self.ball,self.window.width/2, self.window.height-PADDLE_OFFSET-PADDLE_HEIGHT)
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = random.randint(2,INITIAL_Y_SPEED)
        self.paddle_offset = PADDLE_OFFSET
        self.live = lives
        self.frame_rate = FRAME_RATE
        i = 0
        j = 0
        while i < 11 and j <10:    #this part is for making bricks, through two variables, I stimulate the row and columns of bricks
            if i < 10:
                brick_i = GRect(brick_width, brick_height)
                self.window.add(brick_i, x=0 + i *( brick_width + brick_spacing), y=brick_offset + j* (brick_height + brick_spacing))
                if j < 2:
                    brick_i.filled = True
                    brick_i.fill_color = "red"
                elif j < 4:
                    brick_i.filled = True
                    brick_i.fill_color = "orange"
                elif j < 6:
                    brick_i.filled = True
                    brick_i.fill_color = "yellow"
                elif j < 8:
                    brick_i.filled = True
                    brick_i.fill_color = "green"
                elif j < 10:
                    brick_i.filled = True
                    brick_i.fill_color = "blue"
                i += 1
            elif i == 10:

                j += 1
                i = 0
            elif j == 10:
                break
            onmousemoved(self.paddle_move)
            onmouseclicked(self.ball_move)

    def ball_move(self,event):

        if self.ball.x == self.window.width/2 and self.ball.y == self.window.height-self.paddle_height-PADDLE_OFFSET:
            while self.live >0:

                pause(self.frame_rate)
                self.detect_object()
                self.ball.move(self.__dx,self.__dy)
                if self.ball.x >= self.window.width or self.ball.x <= 0:
                    self.__dx = - self.__dx
                elif self.ball.y <= 0:
                    self.__dy = - self.__dy
                elif self.ball.y >= self.window.height:
                    self.live -= 1
                    break
            self.reset_ball_position()
            #self.window.add(self.ball,self.window.width/2 , self.window.height-self.paddle_height-PADDLE_OFFSET)





    """
    def ball_move_velocity(self):
            self.dx = random.randint(1, MAX_X_SPEED)
            self.dy = random.randint(2, INITIAL_Y_SPEED)
            if (random.random()) > 0.5:
                self.dx = -self.dx
            if (random.random()) > 0.5:
                self.dy = -self.dy
            self.ball.move(self.dx,self.dy)
            """


    def paddle_move(self, event):
        """
        this function is for onmousemoved
        to create a moving paddle

        """
        self.paddle.x = event.x - self.paddle.width/2
        self.paddle.y = self.window.height -PADDLE_OFFSET


    def detect_object(self):
        """
        this function is built to sense the brick and the paddle correcrtly
        """
        obj_left_up = self.window.get_object_at(self.ball.x,self.ball.y) #左上角
        obj_left_down = self.window.get_object_at(self.ball.x, self.ball.y +2 * BALL_RADIUS)
        obj_right_up = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
        obj_right_down = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y +2 * BALL_RADIUS)

        if self.ball.y < self.window.height - PADDLE_OFFSET- 2*self.paddle_height:
            #if obj_right_down is None and obj_left_down is None:
            if obj_left_up is not None:
                self.__dy = -self.__dy
                self.remove_stuff(obj_left_up)
                if obj_right_up is not None:
                    self.remove_stuff(obj_right_up)

            #if obj_right_up is None and obj_left_up is None:
            if obj_left_down is not None:
                self.remove_stuff(obj_left_down)
                self.__dy = -self.__dy
                if obj_right_down is not None:
                    self.remove_stuff(obj_right_down)

            #if obj_right_up is None and obj_right_down is None:
            if obj_left_up is not None:
                self.remove_stuff(obj_left_up)
                self.__dx = -self.__dx
                if obj_left_down is not None:
                    self.remove_stuff(obj_left_down)

            #if obj_left_up is None and obj_left_down is None:
            if obj_right_up is not None:
                self.remove_stuff(obj_right_up)
                self.__dx = -self.__dx
                if obj_right_down is not None:
                    self.remove_stuff(obj_right_down)

        if self.ball.y >= self.window.height - PADDLE_OFFSET- self.paddle_height:
            if obj_left_down is not None or obj_right_down is not None:
                self.__dy = -self.__dy

    def remove_stuff(self, obj):
        self.window.remove(obj)

    def reset_ball(self):
        """"
        if the ball drops beneath window.height, we will reset the ball
        """
        self.reset_ball_position()


    def reset_ball_position(self):
        """
        and we need to reset the position of the ball
        """
        self.ball.x = self.window.width/2
        self.ball.y = self.window.height-PADDLE_OFFSET-PADDLE_HEIGHT

    def reset_ball_velocity(self):
        """
        reset the ball velocity also

        """
        self.__dx = random.randint(2,MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if (random.random()) > 0.5:
            self.__dx = -self.__dx











           # self.ball = GOval(ball_radius,ball_radius)
        #self.ball.filled = True
        #self.ball.fill_color = "darkred"
        #self.window.add(self.ball,self.window.width/2, self.window.height-PADDLE_OFFSET-PADDLE_HEIGHT)


        # Center a filled ball in the graphical window.
        # Default initial velocity for the ball.

        # Initialize our mouse listeners.
        # Draw bricks.



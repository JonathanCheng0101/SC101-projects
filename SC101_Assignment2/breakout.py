"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
name:jonathan cheng
"""

from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmousemoved, onmouseclicked
FRAME_RATE = 1000 / 120 # 120 frames per second.


def main():
    graphics = BreakoutGraphics()








"""
    if graphics.ball.x ==graphics.window.width/2 and graphics.ball.y == graphics.window.height-graphics.paddle_offset-graphics.paddle_height:
        while lives > 0:
            pause(FRAME_RATE * 2)
            graphics.detect_object()

            graphics.ball.move(graphics.dx, graphics.dy)

            if graphics.ball.x >= graphics.window.width or graphics.ball.x <= 0:
                graphics.dx = - graphics.dx
            elif graphics.ball.y <= 0:
                graphics.dy = - graphics.dy
            elif graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                break
"""




if __name__ == '__main__':
    main()

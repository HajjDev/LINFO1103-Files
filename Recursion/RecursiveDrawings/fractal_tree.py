import turtle
import math


class FractalTree:
    def __init__(self, order=8):
        # initialize a fresh turtle window to draw in
        self.window = turtle.Screen()
        self.window.clear()
        self.window.delay(0)
        # initialize a new turtle
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10)
        # draw a fractal tree of specified order
        self.draw_tree(n=order, x=75, y=-400.0, angle=math.pi/2, branch_length=300)

    def draw_line(self, x1, y1, x2, y2):
        # draw a line segment from (x1,y1) to (x2, y2)
        self.turtle.penup()
        self.turtle.goto(x1, y1)
        self.turtle.pendown()
        self.turtle.goto(x2, y2)

    def draw_tree(self, n, x, y, angle, branch_length):
        """
        pre: n is a positive integer
        pre: branch_length is strictly positive
        post: draw a fractal tree of order n rooted in (x, y)
        param angle: angle (in radians) of the main branch wrt the horizontal line
        """
        # compute coordinates and width of main branch
        cx = x + math.cos(angle)*branch_length
        cy = y + math.sin(angle)*branch_length
        self.turtle.pensize(math.pow(n, 1.2))
        self.draw_line(x, y, cx, cy)
        if n == 0:  # base case
            return
        # recursively draw right branch, left branch and middle branch as fractal trees of order n-1
        bend_angle = math.radians(15)
        branch_angle = math.radians(37)
        branch_ratio = .65
        self.draw_tree(n - 1, cx, cy, angle + bend_angle - branch_angle, branch_length * branch_ratio)
        self.draw_tree(n - 1, cx, cy, angle + bend_angle + branch_angle, branch_length * branch_ratio)
        self.draw_tree(n - 1, cx, cy, angle + bend_angle, branch_length * (1-branch_ratio))

    def save(self, filename):
        # save current FractalTree drawing to postscript file
        self.window.getcanvas().postscript(file=filename)
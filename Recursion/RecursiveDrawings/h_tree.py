import turtle

class Htree:
    def __init__(self, order=5):
        # initialize a fresh turtle window to draw in
        self.window = turtle.Screen()
        self.window.clear()
        self.window.delay(0)
        # initialize a new turtle
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.pensize(2)
        self.turtle.speed(10)
        # draw a Htree of specified order
        self.draw(n=order, x=0.0, y=0.0, size=300)

    def draw_line(self, x1, y1, x2, y2):
        self.turtle.penup()
        self.turtle.goto(x1, y1)
        self.turtle.pendown()
        self.turtle.goto(x2, y2)

    def draw_h(self, x, y, size):
        # compute coordinates of the H
        x0 = x - size / 2
        x1 = x + size / 2
        y0 = y - size / 2
        y1 = y + size / 2
        # draw the 3 line segments of the H
        self.draw_line(x0, y0, x0, y1)  # left  vertical segment
        self.draw_line(x1, y0, x1, y1)  # right vertical segment
        self.draw_line(x0, y, x1, y)  # horizontal segment

    def draw(self, n, x, y, size):
        if n == 0:  # base case
            return
        self.draw_h(x, y, size)
        # compute x- and y-coordinates of the 4 half-size H-trees
        x0 = x - size / 2
        x1 = x + size / 2
        y0 = y - size / 2
        y1 = y + size / 2
        # recursively draw 4 half-size H-trees of order n-1
        self.draw(n - 1, x0, y0, size / 2)  # lower left  H-tree
        self.draw(n - 1, x1, y0, size / 2)  # lower right H-tree
        self.draw(n - 1, x1, y1, size / 2)  # upper right H-tree
        self.draw(n - 1, x0, y1, size / 2)  # upper left  H-tree

    def save(self, filename):
        # save current Htree drawing to postscript file
        self.window.getcanvas().postscript(file=filename)
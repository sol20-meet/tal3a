from turtle import *
import turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        self.x = x
        self.y = y
    def move(self,screen_width,screen_height):
        new_x = self.x + self.dx
        new_y = self.y + self.dy
        #7dood el tab m3 el borders
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        top_side_ball = new_y + self.r
        bottom_side_ball = new_y-self.r
        #t7rk ll position el jdeed
        self.goto(new_x,new_y)
        self.x = new_x
        self.y = new_y
        
        if (left_side_ball <= -screen_width):
            self.dx = -self.dx
        elif (right_side_ball >= screen_width):
            self.dx = -self.dx
        elif(top_side_ball >= screen_height):
            self.dy = -self.dy
        elif (bottom_side_ball <= -(screen_height)):
            self.dy = -self.dy

    def new_Ball(self,x,y,dx,dy,r,color):
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)

    def Getradius(self):
        return self.r


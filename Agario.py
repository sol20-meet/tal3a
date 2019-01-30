import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()


running = True

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

numbers_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -3
maximum_ball_dx = 3
minimum_ball_dy = -3
maximum_ball_dy = 3

my_ball=Ball(3,3,4,5,60,"yellow")

balls = []
#If you want a random number between values a and b, call:
# random.randint(a, b)
for i in range (numbers_of_balls):
    X = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    Y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
    DX = random.randint(minimum_ball_dx,maximum_ball_radius)
    while DX == 0:
        DX = random.randint(minimum_ball_dx,maximum_ball_radius)
    DY = random.randint(minimum_ball_dy,maximum_ball_radius)
    while DY == 0:
        DY = random.randint(minimum_ball_dy,maximum_ball_radius)
    radius = random.randint(minimum_ball_radius, maximum_ball_radius)
    color = (random.random(),random.random(),random.random())
    other_ball = Ball(X,Y,DX,DY,radius,color)
    balls.append(other_ball)

def move_all_balls():
    for i in balls:
        i.move(screen_width,screen_height)
        
def collide(ball_a,ball_b):
        if ball_a==ball_b:
            return False
        else:
            #print("ball a equals to ball_b")
            distance = math.sqrt(math.pow(ball_a.x - ball_b.x,2) + math.pow(ball_a.y-ball_b.y,2))
            if distance <= ball_a.r + ball_b.r:
                return True
            else:
                return False
        
def check_all_balls_collision():
    global running
    all_balls=[]
    all_balls.append(my_ball)
    for ball in balls:
        all_balls.append(ball)

    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a,ball_b):
                r1 = ball_a.r
                r2 = ball_b.r
                X = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
                Y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
                DX = random.randint(minimum_ball_dx,maximum_ball_radius)
                while DX == 0:
                    DX = random.randint(minimum_ball_dx,maximum_ball_radius)
                DY = random.randint(minimum_ball_dy,maximum_ball_radius)
                while DY == 0:
                    DY = random.randint(minimum_ball_dy,maximum_ball_radius)
                radius = random.randint(minimum_ball_radius, maximum_ball_radius)
                color = (random.random(),random.random(),random.random())

                                             
                if r1 < r2:
                    if ball_a == my_ball:
                        print("GameOver")
                        running = False
                    else:
                        ball_b.r +=1
                        ball_b.shapesize(ball_b.r/10)
                        ball_a.new_Ball(X,Y,DX,DY,radius,color)
                else:
                    if ball_b == my_ball:
                        print("GameOver")
                        running = False
                    else:
                        ball_a.r +=1
                        ball_a.shapesize(ball_a.r/10)
                        ball_b.new_Ball(X,Y,DX,DY,radius,color)
def move_around():
    X_Coordinate = turtle.getcanvas().winfo_pointerx() - screen_width * 2
    Y_Coordinate = screen_height - turtle.getcanvas().winfo_pointery()
    my_ball.x = X_Coordinate
    my_ball.y = Y_Coordinate
    my_ball.goto(X_Coordinate,Y_Coordinate)

while running:
    if not screen_width == turtle.getcanvas().winfo_width() and screen_height == turtle.getcanvas().winfo_height():
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
    move_around()
    move_all_balls()
    check_all_balls_collision()
    turtle.update()
    time.sleep(0.2)
    
turtle.mainloop()

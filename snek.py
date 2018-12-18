import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

#screen
wn = turtle.Screen()
wn.title("Snek")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#snek hed
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"



#snek food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Hcore: 0", align="center", font=("Courier", 24, "normal"))
#functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def stop():
    head.direction = "stop"

    
def move():


    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def gameover():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    #hide the segments
    for segment in segments:
        segment.goto(1000,1000)
    #clear the segments
    segments.clear()
    score = 0
    pen.clear()
    pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    currenttime = time.asctime()
    print (currenttime)

#keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(stop, "space")

#the loop a
while True:
    wn.update()

    #border collision check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        gameover()

    #head body collision check
    for segment in segments:
        if segment.distance(head) < 20:
            gameover()

    #food eaten    
    if head.distance(food) < 20:
        x = random.randint(-14, 14)
        y = random.randint(-14, 14)
        food.goto(x*20, y*20)
        #add tail
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        #increace score
        score += 10
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
     

    move()

    time.sleep(delay)


wn.mainloop()

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer()


# Score
score_a = 0
score_b = 0


#
name_a = input("Player A name: ")
name_b = input("Player B name: ")

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)  #ANIMATION SPEED, not movement speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0) #ANIMATION SPEED, not movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{name_a}: 0  {name_b}: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up():
    y = paddle_a.ycor() #y = actual coordinates of the paddle a
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #y = actual coordinates of the paddle a
    y += -20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor() #y = actual coordinates of the paddle b
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #y = actual coordinates of the paddle b
    y += -20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(name_a,score_a,name_b, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(name_a, score_a, name_b, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)                                                              #would ball bouncing work without this line???
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
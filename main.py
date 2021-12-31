"""
Main file of the Pong Game
With Turtle module
In Python
By Ulysse Valdenaire
"""
import turtle

#we create the window
window = turtle.Screen()
window.title("Game Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#we create the Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#we create the Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#we create the Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy =  0.3

#Score
score_a = 0
score_b = 0

#we create the pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0", align = "center", font = ("courier", 24, "normal"))

#Moving functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up, "z")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "o")
window.onkeypress(paddle_b_down, "l")

# Main game loop
while True:
    window.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50 ):
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
### Imports ###
import turtle
import random


# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)


# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0
hit_ball.dy = 0

circleDirection = random.choice(["left", "right"])

if circleDirection == "left":
    hit_ball.dx = 5
else:
    hit_ball.dx = -5


# Initialize the score
left_player = 0
right_player = 0


# Displays the score

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("0 : 0", align="center", font=("Courier", 24, "normal"))

def resetPad():
    left_pad.goto(-400, 0)
    right_pad.goto(400, 0)


class PaddleMovement:
    def __init__(self):
        self.self = self
    
    def paddleaup():
        y = left_pad.ycor()
        y += 20
        left_pad.sety(y)


    def paddleadown():
        y = left_pad.ycor()
        y -= 20
        left_pad.sety(y)


    def paddlebup():
        y = right_pad.ycor()
        y += 20
        right_pad.sety(y)


    def paddlebdown():
        y = right_pad.ycor()
        y -= 20
        right_pad.sety(y)
    

# Keyboard bindings
sc.listen()
sc.onkeypress(PaddleMovement.paddleaup, "w")
sc.onkeypress(PaddleMovement.paddleadown, "s")
sc.onkeypress(PaddleMovement.paddlebup, "Up")
sc.onkeypress(PaddleMovement.paddlebdown, "Down")


while True:
	sc.update()

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

	# Checking borders
	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280:
		hit_ball.sety(-280)
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		left_player += 1
		sketch.clear()
		sketch.write("Player One : {} Player Two: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))
        resetPad()

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		right_player += 1
		sketch.clear()
		sketch.write("Player One : {} Player Two: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))
        resetPad()

	# Paddle ball collision
	if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40):
		hit_ball.setx(360)
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
		hit_ball.setx(-360)
		hit_ball.dx*=-1

### Image ###
# https://www.google.com/search?q=create+pong+in+python+board&rlz=1C1GCEB_enGB978GB978&hl=en&tbm=isch&source=iu&ictx=1&fir=ZuRtlgqOLCAs3M%252C98ebYjHXFBlIaM%252C_&vet=1&usg=AI4_-kShZZJULG_Y_uqAxMsuOkKNIfh_RQ&sa=X&ved=2ahUKEwiCi6-Bx730AhWsQEEAHYAZCCIQ9QF6BAgFEAE&biw=786&bih=779&dpr=1&surl=1&safe=active&ssui=on#imgrc=ZuRtlgqOLCAs3M
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle

### Imports ###
import turtle
from constants import *

### Turtle Screen ###
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor(WHITE)
screen.setup(width=WIDTH, height=HEIGHT)

class Game():
    def __init__(self):
        self.score = 0
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color(BLACK)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2
        self.paddles()
        self.score_board()
    
    def paddles(self):
        left_paddle = turtle.Turtle()
        left_paddle.speed(0)
        left_paddle.shape("square")
        left_paddle.color(BLACK)
        left_paddle.shapesize(stretch_wid=6, stretch_len=2)

        right_paddle = turtle.Turtle()
        right_paddle.speed(0)
        right_paddle.shape("square")
        right_paddle.color(BLACK)
        right_paddle.shapesize(stretch_wid=6, stretch_len=2)

    def game_over(self):
        if self.ball.ycor() > HEIGHT:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()

    def score_board(self):
        self.score_a = turtle.Turtle()
        self.score_a.speed(0)
        self.score_a.color(BLACK)
        self.score_a.penup()
        self.score_a.setposition(-WIDTH/2 + 20, HEIGHT/2 - 20)
        self.score_a.write(self.score, font=("Arial", 20, "normal"))

    def move_paddle(self):
        if self.ball.ycor() > HEIGHT:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()
        
        elif self.ball.ycor() < -HEIGHT:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()

        elif self.ball.xcor() > WIDTH:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()
        
        elif self.ball.xcor() < -WIDTH:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()
        
        elif self.ball.xcor() > WIDTH/2:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()
        
        elif self.ball.xcor() < -WIDTH/2:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score += 1
            self.score_board()
    
    def move_ball(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        


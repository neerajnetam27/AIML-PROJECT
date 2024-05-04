import turtle

import time

import random

delay = 0.1

# SCORE

score = 0

high_score = 0

# SETTING UP THE SCREEN

wn = turtle.Screen()

wn.title("SnakeX")

wn.bgcolor("Black")

wn.setup(width=600, height=600)

wn.tracer(0)  # turns off the screen updates

# SNAKE HEAD

head = turtle.Turtle()

head.speed(0)

head.shape("circle")

head.color("white")

head.penup()

head.goto(0, 0)

head.direction = "stop"

# SNAKE FOOD

food = turtle.Turtle()

food.speed(0)

food.shape("circle")

food.color("red")

food.penup()

food.goto(0, 100)

segments = []

# SCORE

pen = turtle.Turtle()

pen.speed(0)

pen.shape("square")

pen.color("yellow")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Score: 0   Highest Score: 0", align="center", font=("Courier", 24, "normal"))


# FUNCTIONS

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

    # KEYBOARD BINDING


wn.listen()

wn.onkeypress(go_up, "Up")

wn.onkeypress(go_down, "Down")

wn.onkeypress(go_left, "Left")

wn.onkeypress(go_right, "Right")

# MAIN GAME LOOP

while True:

    wn.update()

    # CHECK FOR COLLISION WITH THE BORDER

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 230 or head.ycor() < -290:

        time.sleep(1)

        head.goto(0, 0)

        head.direction = "stop"

        # HIDE THE SEGMENTS

        for segment in segments:
            segment.goto(1000, 1000)

            # CLEAR THE SEGMENTS LIST

        segments.clear()

        # RESET THE SCORE

        score = 0

        # RESET THE DELAY

        delay = 0.1

        # UPDATE THE SCORE DISPLAY

        pen.clear()

        pen.write("Score: {}  Highest Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # CHECK FOR THE COLLISION WITH FOOD

    if head.distance(food) < 20:

        # move the food to a random spot

        x = random.randint(-290, 290)

        y = random.randint(-290, 230)

        food.goto(x, y)

        # ADD A SEGMENT

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("grey")

        new_segment.penup()

        segments.append(new_segment)

        # SHORTEN THE DELAY

        delay -= 0.001

        # THIS IS TO COUNT THE SCORE INCREASE THE SCORE

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()

        pen.write("Score: {}  Highest Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # MOVE THE END SEGMENTS FIRST IN THE REVERSE ORDER

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()

        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

        # MOVE THE SEGMENT 0 TO WHERE THE HEAD IS

    if len(segments) > 0:
        x = head.xcor()

        y = head.ycor()

        segments[0].goto(x, y)

    move()

    # THIS IS TO CHECK FOR COLLISION WITH THE BODY OF SNAKE ITSELF

    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)

            head.direction = "stop"

            # HIDE THE SEGMENTS

            for segment in segments:
                segment.goto(1000, 1000)

                # CLEAR THE SEGMENTS LIST

            segments.clear()

            # RESET THE SCORE

            score = 0

            # RESET THE DELAY

            delay = 0.1

            # UPDATE THE SCORE DISPLAY

            pen.clear()

            pen.write("Score: {}  Highest Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
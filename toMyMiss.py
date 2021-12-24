import turtle
import random
import time

width = height = 500

window = turtle.Screen()
window.setup(width, height)
window.bgcolor("sky blue")
window.title("Happy Holidays")

snowball_rate = 1, 3
snowball_size = 5, 15
wind_change = 1, 5
max_wind = 3

# Create all circle-shaped objects


def make_circle(turtle_name, x, y, size, colour):
    turtle_name.color(colour)
    turtle_name.penup()
    turtle_name.setposition(x, y)
    turtle_name.dot(size)


# Create new snowballs and store in list
list_of_snowballs = []


def make_snowball():
    snowball = turtle.Turtle()
    snowball.color("white")
    snowball.penup()
    snowball.setposition(random.randint(-2*width, width/2), height/2)
    snowball.hideturtle()
    snowball.size = random.randint(*snowball_size)
    list_of_snowballs.append(snowball)


def move_snowball(turtle_name, falling_speed=1, wind=0):
    turtle_name.clear()
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    if wind:
        turtle_name.setx(turtle_name.xcor() + wind)
    turtle_name.dot(turtle_name.size)


# Snowman: body
snowman = turtle.Turtle()
x_position = 0
y_positions = 75, 0, -100
size = 75
for y in y_positions:
    make_circle(snowman, x_position, y, size, "white")
    size = size * 1.5

# Snowman: buttons
button_seperation = 25
button_y_positions = [y_positions[1]-button_seperation,
                      y_positions[1],
                      y_positions[1]+button_seperation]
for y in button_y_positions:
    make_circle(snowman, x_position, y, 10, "black")

# Snowman: eyes
y_offset = 10
x_seperation = 15
for x in x_position-x_seperation, x_position+x_seperation:
    make_circle(snowman, x, y_positions[0] + y_offset, 20, "green")
    make_circle(snowman, x, y_positions[0] + y_offset, 10, "black")

# Snowman: nose
snowman.color("orange")
snowman.setposition(x_position - 10, y_positions[0]-y_offset)
snowman.shape("triangle")
snowman.setheading(200)
snowman.turtlesize(0.5, 2.5)

window.tracer(0)

# Ground
grass = turtle.Turtle()
grass.fillcolor("forest green")
grass.penup()
grass.setposition(-width/2, -height/2)
grass.begin_fill()
for _ in range(2):
    grass.forward(width)
    grass.left(90)
    grass.forward(70)
    grass.left(90)
grass.end_fill()

ground = turtle.Turtle()
for x in range(int(-width/2), int(width/2), int(width/200)):
    make_circle(ground, x, -180, random.randint(5, 20), "white")

text = turtle.Turtle()
text.color("red")
text.penup()
text.setposition(-100, 170)
text.write("Happy Holidays", font=(
    "Apple Chancery", 30, "bold"), align="center")
text.setposition(130, 140)
text.color("dark green")
text.write("Jed", font=("Avenir", 30, "bold"), align="right")
text.color("black")
text.write("Du", font=("Avenir", 30, "normal"), align="left")
text.setx(50)
text.write("from", font=("Apple Chancery", 20, "bold"), align="right")
text.hideturtle()

time_delay = 0
start_time = time.time()
wind = 0
wind_delay = 5
wind_timer = time.time()
wind_step = 0.1
while True:
    if time.time() - start_time > time_delay:
        make_snowball()
        start_time = time.time()
        time_delay = random.randint(*snowball_rate)/10

    for snowball in list_of_snowballs:
        move_snowball(snowball, wind=wind)
        if snowball.ycor() < -height/2:
            snowball.clear()
            list_of_snowballs.remove(snowball)

    if time.time() - wind_timer > wind_delay:
        wind += wind_step
        if wind >= max_wind:
            wind_step = -wind_step
        elif wind <= 0:
            wind_step = abs(wind_step)

        wind_timer = time.time()
        wind_delay = random.randint(*wind_change)/10

    window.update()

turtle.done()

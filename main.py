from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("gray")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
race_is_active = False
user_guess = screen.textinput(title="Turtle Racing Game",
                              prompt="Which turtle will win the race?\n\nEnter a color: "
                                     "red, orange, yellow, green, blue, purple\n").lower()

x_position = -240
y_position = 120

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")  # 40 by 40 object in the canvas
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=y_position)
    y_position -= 40
    all_turtles.append(new_turtle)

if user_guess:
    race_is_active = True

while race_is_active:
    for turtle_index in all_turtles:
        if turtle_index.xcor() >= 230:  # finishing line at x = 500/2-40/2 = 230
            race_is_active = False
            winner = turtle_index.pencolor()
            if winner == user_guess:
                print(f"おめでとうございます！{winner}が勝ちました！")
            else:
                print(f"惜しいです！{winner}カメが勝ちました！")
        random_moving_distance = random.randint(0, 12)
        turtle_index.forward(random_moving_distance)

screen.exitonclick()

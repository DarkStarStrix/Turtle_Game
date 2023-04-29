from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

# # turtle race game between 4 turtles
#
# screen.setup(width=500, height=400)
# user_bot = screen.textinput(title="make your bet", prompt="which turtle will win the race ? Enter a color: ")
#
# timmy.shape("turtle")
# timmy.color("red")
# timmy.penup()
# timmy.goto(x=-230, y=-100)
#
# Johnny = Turtle()
# Johnny.shape("turtle")
# Johnny.color("blue")
# Johnny.penup()
# Johnny.goto(x=-230, y=-70)
#
# Sally = Turtle()
# Sally.shape("turtle")
# Sally.color("green")
# Sally.penup()
# Sally.goto(x=-230, y=-40)
#
# Billy = Turtle()
# Billy.shape("turtle")
# Billy.color("yellow")
# Billy.penup()
# Billy.goto(x=-230, y=-10)
#
# if timmy.xcor() > 230:
#     print("red wins")
#
# if Johnny.xcor() > 230:
#     print("blue wins")
#
# if Sally.xcor() > 230:
#     print("green wins")
#
# if Billy.xcor() > 230:
#     print("yellow wins")
#
# while timmy.xcor() < 230 and Johnny.xcor() < 230 and Sally.xcor() < 230 and Billy.xcor() < 230:
#     timmy.forward(random.randint(0, 10))
#     Johnny.forward(random.randint(0, 10))
#     Sally.forward(random.randint(0, 10))
#     Billy.forward(random.randint(0, 10))


# # Etch a sketch
# def move_forwards():
#     timmy.forward(10)
#
#
# def move_backwards():
#     timmy.backward(10)
#
#
# def turn_left():
#     timmy.left(10)
#
#
# def turn_right():
#     timmy.right(10)
#
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()

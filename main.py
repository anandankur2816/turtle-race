from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
is_race_on = False
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
y_pos = [-50, -25, 0, 25, 50, 75]
user_bet = screen.textinput('Place your bet', 'Which turtle will win')
if user_bet:
    is_race_on = True
all_t = []
for _ in range(0, 6):
    t = Turtle()
    # t.speed(0)
    t.shape('turtle')
    t.penup()
    t.goto(-230, y_pos[_])
    t.color(colors[_])
    all_t.append(t)

while is_race_on:
    for _ in all_t:
        rd = random.randint(0, 10)
        _.forward(rd)
        if _.pos()[0] >= 250:
            print(f"Race is over.{_.color()[0]}  turtle won the race")
            if user_bet == _.color()[0]:
                print("You won the bet")
            else:
                print("You lost the bet")
            is_race_on = False
            break


screen.exitonclick()

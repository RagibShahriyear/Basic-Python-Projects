import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# 1. Convert the guess to Title case


# 2. Check if the guess is among the 50 states and write correct guesses onto the map
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                     prompt="What's another state?")).title()

    # Not using list comprehension
    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_learn.csv")

    # Using list comprehension
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(state_data.state.item())

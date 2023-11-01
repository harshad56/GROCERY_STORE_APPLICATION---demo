
# day-25 us game is in folder

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct",
                                    prompt="What a another state's name").title()
    print(answer_state)

    if answer_state == "Exit".title():

        # --------------------------------------------------------------------------------
        # using list comprehension
        missing_states = [
            state for state in all_states if state not in guessed_state]
        # ---------------------------------------------------------------------------------
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn_state.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

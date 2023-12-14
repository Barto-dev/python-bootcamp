import turtle
from turtle import Screen, Turtle
import pandas

IMAGE = "blank_states_img.gif"
PROMPT = "What's another state's name?"
guesses = []
is_game_on = True

screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)

data = pandas.read_csv("states.csv")
all_states = data.state.to_list()
print(all_states)
states_count = len(data.state)

while is_game_on:
    answer_state = screen.textinput(
        title=f"{len(guesses)}/{states_count} correct", prompt=PROMPT
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guesses]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states:
        state_row = data[data.state == answer_state]
        state_name = state_row.state.item()
        timmy = Turtle()
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(x=int(state_row.x), y=int(state_row.y))
        timmy.write(state_name)
        guesses.append(state_name)

    if len(guesses) == states_count:
        print("You got all the states!")
        break


turtle.mainloop()

import pandas
from turtle import Turtle, Screen

image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S States Game")
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].str.lower()

is_game_running = True
guessed_states = []

while is_game_running:
    screen.update()
    if len(guessed_states) < 50:
        answer_state = screen.textinput(title = f"{len(guessed_states)}/50 Stetes Correct",
                                       prompt = "What's another state's name?")
        if answer_state in all_states:
            guessed_states.append(answer_state.lower())
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            state_data = data[data["state"] == answer_state.lower()]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(arg=f"{answer_state.capitalize()}", font=("Courier", 8, "normal"))
        
        elif len(guessed_states) == 50:
            print("You have guessed all 50 states!")
            is_game_running = False

screen.mainloop()
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                    prompt = "What's another state's name?").title()
    # .title() 메소드는 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    elif len(guessed_states) == 50:
        print("You have guessed all 50 states!")
        break
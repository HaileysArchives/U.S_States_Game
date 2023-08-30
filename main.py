import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image) # turtle 펜 모양 변경

def get_mouse_click(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click)

turtle.mainloop() # 코드가 실행을 끝내도 화면이 계속 열려있는 방법

answer_state = screen.textinput(title = "Guess the State", prompt = "What's another state's name?")
print(answer_state)

# screen.exitonclick()
FONT = ("Arial", 10, "normal")


from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
pencil = Turtle()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
pencil.penup()
pencil.hideturtle()

data = pandas.read_csv("50_states.csv")
all_state_list = data.state.to_list()
# series -> list 전환
game_is_on = True
score = 0
correct_guess = []

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"Guess the state ({score}/50 correct) ", prompt="What's another state's name?").title()

    if answer == "Exit":
        # 학습을 위해 프로그램(게임) 종료 후 csv 파일("states_to_learn")에 저장하기.
        states_list_to_learn = []
        for state in all_state_list:
            if state not in correct_guess:
                states_list_to_learn.append(state)
        df = pandas.DataFrame(states_list_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer in all_state_list:
    #list로 바꾸었기 때문에 in 키워드를 이용한 조건문 생성 가능
        score += 1
        correct_guess.append(answer)
        correct_state = data[data.state == answer]
        x_cor = int(correct_state["x"])
        y_cor = int(correct_state["y"])
        pencil.goto(x_cor, y_cor)
        pencil.write(answer, font=FONT)




screen.mainloop()
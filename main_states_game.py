import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("29_states.csv")
all_states = data.state.to_list()

guessed_state = []
chances = 0

while len(guessed_state) < 29:

    answer = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state name?").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        """for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)"""
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer in all_states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)

    if len(guessed_state) == 29:
        t.goto(150,-200)
        t.write("You win", align="center", font=("Courier", 40, "bold"))

    if answer not in all_states:
        chances += 1
        if chances == 3:
            t.goto(150, -200)
            t.write("You Loose", align="center", font=("Courier", 40, "bold"))


screen.exitonclick()
import turtle
import pandas
from states_manager import StatesManager

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_manager = StatesManager()

all_states = pandas.read_csv('50_states.csv')
state_names = all_states.state.to_list()

while not states_manager.all_states_guessed():

    answer_input = turtle.textinput(title=f'{states_manager.score}/50 the State',
                                    prompt="Guess another state's name").title()

    if answer_input == 'Exit':
        states_manager.states_to_learn(state_names)
        break

    elif answer_input in state_names:
        new_state = all_states[all_states.state == answer_input]
        position = (int(new_state.x), int(new_state.y))
        states_manager.add_name(answer_input, position)


# screen.mainloop()

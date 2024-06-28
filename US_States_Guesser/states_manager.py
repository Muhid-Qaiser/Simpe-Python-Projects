from turtle import Turtle
import pandas

TOTAL_STATES = 50


class StatesManager:

    def __init__(self):
        super().__init__()
        self.score = 0
        self.states = []

    def add_name(self, name, position):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(position)
        new_state.write(name)
        self.states.append(name)
        self.score += 1

    def all_states_guessed(self):
        return TOTAL_STATES == self.score

    def get_score(self):
        return self.score

    def states_to_learn(self, all_states):
        states_missed = [state for state in all_states if state not in self.states]
        self.convert_to_csv(states_missed)

    def convert_to_csv(self, states_missed):
        new_data = pandas.DataFrame(states_missed)
        new_data.to_csv("states_to_learn.csv")

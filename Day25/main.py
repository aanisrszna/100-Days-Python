import turtle
import pandas

# Set up the screen and image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Get the user's guess
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()  # Capitalize to match the format in CSV

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        # Track guessed states
        guessed_states.append(answer_state)

        # Create a turtle to write the state name at the correct location
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get the x and y coordinates for the guessed state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))

        # Write the state name at the guessed state's location
        t.write(answer_state)

# Optionally, save missing states to a CSV file
missing_states = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()

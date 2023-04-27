import turtle
import pandas
import time


TRACKER=0
screen = turtle.Screen()
screen.title("US map")
img = ".//us-states-game-start\\blank_states_img.gif"
screen.addshape(img)
screen.setup(width=740,height=510)
screen.tracer(1)
turtle.shape(img)

def get_data(state_ = None):
    global TRACKER
    state_=state_.capitalize()
    data = pandas.read_csv(".//us-states-game-start\\50_states.csv")
    if state_ in data.state.to_list():
        TRACKER+=1
        row = data[data['state'] == state_]
        x = row['x'].values[0]
        y = row['y'].values[0]
        turtle_state=turtle.Turtle()
        turtle_state.penup()
        
        turtle_state.hideturtle()
        turtle_state.goto(x,y)
        turtle_state.write(f"{state_}")
        return True
    else:
        return(False)

def print_coordinates(x, y):
    print("Clicked at x={}, y={}".format(x, y))
turtle.onscreenclick(print_coordinates)

game_over=False

while not game_over:
    get_input = turtle.textinput(f"State Name. {TRACKER}/50. Just click OK to leave the game.", "Enter State Name: ")
    if len(get_input)==0:
        game_over=True
    if not get_data(get_input):
        end_game_text=turtle.Turtle()
        end_game_text.penup()
        end_game_text.hideturtle()
        end_game_text.write("GAME OVER", font=("Arial", 19, "bold"))
        game_over=True



screen.exitonclick()
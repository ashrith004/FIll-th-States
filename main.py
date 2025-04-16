import turtle
import pandas 

screen = turtle.Screen()
screen.title("INDIA STATE GAME") 
screen.setup(width=800, height=800)
img= "G:/100 PROJECTS/INDIA STATE GAME/india_states.gif"
screen.addshape(img)  # Ensure the file is in the same folder
turtle.shape(img)

data = pandas.read_csv("G:/100 PROJECTS/INDIA STATE GAME/31_states.csv")
all_states = data.state.to_list()
guessed_states =[]
while len(guessed_states) < 31:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 States Correct", 
                                    prompt="What's another state name").title()
    
    if answer_state == "Exist":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.apppend()
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        # t.color("red")
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
    
    
screen.exitonclick()
   
         
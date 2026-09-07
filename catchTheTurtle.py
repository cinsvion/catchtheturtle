import random as r
import turtle
time = 2

score=0
screen=turtle.Screen()
screen.title("Catch the Turtle")
screen.screensize(800,600)
screen.bgcolor("lightblue")
character=turtle.Turtle()
character.speed(0)
character.shape("turtle")
character.color("green")
character.turtlesize(2,2)
character.penup()


score_turtle=turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(-140,300)
score_turtle.turtlesize(3,3)
score_turtle.write("Your score is 0",
                font=("Arial", 30, "normal")
)


time_turtle=turtle.Turtle()
time_turtle.penup()
time_turtle.hideturtle()
time_turtle.goto(-50,250)
time_turtle.turtlesize(3,3)
time_turtle.write(f"Time left: {time} ",)


def gotorandom():
        random_for_x = r.randint(-350, 350)
        random_for_y = r.randint(-250, 250)
        character.goto(random_for_x,random_for_y)
def startrandom(x,y):
        gotorandom()
        global score
        score +=1
        scoreupdater()
        print(f"Your score is {score}")
def scoreupdater():
    global score
    score_turtle.clear()
    score_turtle.write(f"Your score is {score}",
                       font=("Arial", 30, "normal"))

def timecounter(time):
    time_turtle.clear()
    if time>0:
        print(time)
        time_turtle.write(f"Time left:{time} ")
        screen.ontimer(lambda:timecounter(time - 1),1000)
    else:
        time_turtle.write("GAME OVER")
        character.color("lightblue")



timecounter(time)



turtle.listen()
character.onclick(startrandom)
screen.mainloop()
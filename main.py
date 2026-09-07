import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Drawing Game!")
colors=("blue","purple","black","red")
turtle_instance=turtle.Turtle()
turtle_instance.speed(5)
turtle_instance.pensize(2)
current_index=0
turtle_instance.penup()
#fonksiyonlar
def clean():
    turtle_instance.clear()
def move():
    turtle_instance.forward(50)
def reset():
    turtle_instance.clear()
    turtle_instance.goto(0,0)
    turtle_instance.clear()
def left():
    turtle_instance.left(22.5)
def right():
    turtle_instance.right(22.5)
def change_color():
    global current_index
    current_index=(current_index+1)%len(colors)
    selected_color=colors[current_index]
    turtle_instance.color(selected_color)
def get_click_coord(x, y):
    print(f"Tıklanan Koordinat -> X: {x}, Y: {y}")
def gotoclick(x,y):
    turtle_instance.goto(x, y)

#tuşlar
turtle.listen()
turtle.onkey(move,"w")
turtle.onkey(clean,"s")
turtle.onkey(reset,"r")
turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.onkey(change_color,"m")
drawing_board.onclick(get_click_coord)
drawing_board.onclick(gotoclick)

drawing_board.mainloop()
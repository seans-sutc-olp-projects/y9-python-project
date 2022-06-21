import turtle
exportArray = []
# Turtles
turtle.hideturtle()
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(3)
panel = turtle.Turtle()
panelText = turtle.Turtle()
panel.speed(0)
panelText.speed(0)
drawer.shape("turtle")

# Panel
panel.pu()
panel.left(90)
panel.fd(100)
panel.right(90)
panel.pd()
def panelLongSide():
    panel.fd(200)
    panel.left(90)
def panelShortSide():
    panel.fd(100)
    panel.left(90)
panelLongSide()
panelShortSide()
panel.fd(400)
panel.left(90)
panelShortSide()
panelLongSide()
panel.hideturtle()

def ruinDrawing():
    global formattedInput
    for x in range(len(formattedInput)):
        for y in range(2):
            formattedInput[x][y] = int(round(formattedInput[x][y]/25)*25)

# Panel Text
panelText.pu()
panelText.left(90)
panelText.fd(140)
panelText.left(90)
panelText.fd(180)
panelText.write("Drag the turtle to draw! WARNING: dragging too fast will crash the program")
panelText.right(90)
panelText.bk(39)
panelText.write("THIS WILL NOT BE SAVED")
panelText.hideturtle()

# Drawer
drawer.pu()
drawer.right(90)
drawer.fd(300)
drawer.right(180)  
drawer.showturtle()
drawer.pd()
# Import code:
importValue = turtle.textinput("Project", "Enter the exported Array (enter 0 if you have no export)")
if not importValue == "0":
    importValue = importValue.replace("[", "")
    importValue = importValue.replace("\n", "")
    importValue = importValue.replace("'", "")
    tempValues = importValue.split("], ")
    formattedInput = []
    for y in tempValues:
        y = y.replace("]", "")
        tempPair = y.split(",")
        formattedInput.append([float(tempPair[0]), float(tempPair[1])])
    #ruinDrawing()
    for x in range(len(formattedInput)-1):
        drawer.goto(formattedInput[x][0],formattedInput[x][1])
    exportArray = tempValues
    for z in range(len(exportArray)):
        exportArray[z] = exportArray[z].replace("'", "")
                    
# Drag code
def drag(x,y):
    global exportArray
    drawer.goto(x, y)
    exportArray.append([x, y])
    print("exportArray: ", exportArray)
    drawer.ondrag(drag)

drawer.ondrag(drag)
print("exportArray: ", exportArray)
# Keepalive
turtle.mainloop()

import turtle
import buttons

# Function-Shorthands
dFunct = movement_functions

# Turtles
drawer = turtle.Turtle()
drawer.hideturtle()
panel = turtle.Turtle()
panelText = turtle.Turtle()
panelControlTextArea = turtle.Turtle()
panelControlTextArea.speed(0)
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

# Panel Text
panelText.pu()
panelText.left(90)
panelText.fd(110)
panelText.left(90)
panelText.fd(180)
panelText.write("Hello World")
panelText.hideturtle()

# Drawer
drawer.pu()
drawer.right(90)
drawer.fd(300)
drawer.right(180)  
drawer.showturtle()
drawer.pd()

# Buttons
turtle.onkeypress("w", buttons.forward()




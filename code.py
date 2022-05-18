import turtle

# Turtles
drawer = turtle.Turtle()
drawer.hideturtle()
panel = turtle.Turtle()
panelText = turtle.Turtle()
box = turtle.Turtle()
panel.speed(0)
box.speed(0)
panelText.speed(0)
drawer.shape("turtle")

# Box
box.pu()
box.right(90)
box.fd(300)
box.right(90)
box.fd(150)
box.right(90)
box.pd()
def boxSide():
    box.fd(300)
    box.right(90)
boxSide()
boxSide()
boxSide()
box.fd(300)
box.hideturtle()

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








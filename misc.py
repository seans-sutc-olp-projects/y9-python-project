# Buttons / Text areas
import turtle
def numinput():
    value = turtle.numinput("Project", "Enter a number to action", 50, minval=10, maxval=500)
    return value
def stringinput():
    value = turtle.textinput("Project", "Enter the string to action")
    return value

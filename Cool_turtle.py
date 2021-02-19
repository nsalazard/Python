import turtle

bgcolor = input("Write a color for the background: ")
tesscolor = input("Write a color for Tess: ")
tes = input("Write a number: ")
pentess = int(tes)

wn = turtle.Screen()
wn.bgcolor(bgcolor)        # set the window background color

tess = turtle.Turtle()
tess.color(tesscolor)              # make tess blue
tess.pensize(pentess)                 # set the width of her pen
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2




wn.exitonclick()
#Python

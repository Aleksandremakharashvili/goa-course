
Nia
Nia Khoperia
from turtle import*

#we want to paint a house

#step 1:  draw a square 

speed(20)
width(9)
color("blue")
forward(200)
left(90)  

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#driwing a window

left(120)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(200)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

exitonclick()
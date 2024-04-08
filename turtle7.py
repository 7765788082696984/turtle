import turtle
x=turtle.Turtle()
x.speed(100)
x.width(2.5)
x.color("green")
i=0
while i<200:
    i+=1
    x.fd(i%400)
    x.rt(50)
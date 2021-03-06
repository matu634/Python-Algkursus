"""Kanaelevant."""
import turtle


def turnaround():
    """"Turn the turtle around.

    :return turn right 180 degrees
    """
    return pen.right(180)


pen = turtle.Pen()
pen.speed(10.4)
pen.fillcolor("gray")
pen.shape("turtle")
pen.penup()
pen.right(90)
pen.forward(300)
pen.pendown()
pen.left(90)
pen.circle(200, extent=360)
pen.up()
pen.circle(200, extent=180)
turnaround()
pen.down()
pen.circle(100, extent=360)
pen.up()
pen.circle(100, extent=140)
turnaround()
pen.down()
pen.begin_fill()
pen.circle(55, extent=360)
pen.end_fill()
pen.right(180)
pen.up()
pen.circle(100, extent=80)
turnaround()
pen.down()
pen.begin_fill()
pen.circle(55, extent=360)
pen.end_fill()
turnaround()
pen.up()
pen.circle(100, extent=140)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.down()
pen.fillcolor()
pen.circle(10, extent=360)
pen.left(90)
pen.up()
pen.forward(40)
pen.right(90)
pen.forward(30)


def eye():
    """
    Make an eye.

    :return an eye that is colored black and white
    """
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(20, extent=360)
    pen.end_fill()
    pen.fillcolor("white")
    pen.circle(20, extent=45)
    pen.begin_fill()
    pen.circle(7, extent=360)
    pen.end_fill()
    pen.circle(20, extent=315)
    pen.fillcolor("black")
    turnaround()
    pen.up()


eye()
pen.forward(60)
turnaround()
eye()
turnaround()
pen.forward(30)
pen.right(90)
pen.forward(120)
turnaround()
pen.forward(20)
pen.right(90)
pen.down()
pen.fillcolor("pink")
pen.begin_fill()
pen.circle(25, extent=360)
pen.end_fill()
pen.right(90)
pen.up()
pen.forward(20)
pen.right(90)
pen.circle(200, extent=45)


def jalg():
    """
    Make a leg.

    :return a leg with a rectangle and a half circle that's colored black
    """
    pen.fillcolor("black")
    pen.right(80)
    pen.down()
    pen.forward(80)
    pen.begin_fill()
    pen.circle(30, extent=180)
    pen.end_fill()
    pen.forward(79)
    pen.left(90)
    pen.up()
    pen.forward(60)
    pen.right(90)
    pen.forward(1)
    pen.right(100)


jalg()
pen.circle(200, extent=90)
jalg()
pen.circle(200, extent=70)
jalg()
pen.circle(200, extent=90)
jalg()
pen.circle(200, extent=160)
pen.down()
turnaround()
pen.circle(200, extent=45)
pen.circle(100, extent=180)
turnaround()
pen.up()
turtle.done()

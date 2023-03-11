import turtle

c = turtle.Screen()
t = turtle.Turtle()


def draw_figure(side_count, side_size):
    angle = int(360 / side_count)

    #t.lt(90)

    for i in range(0, side_count):
        t.fd(side_size)
        t.rt(angle)

def main():
    t.speed(100)
    turtle.bgcolor("black")
    t.pencolor("orange")

    for i in range(10, 300, 3):
        draw_figure(10, i)
        t.rt(10)
        
main()

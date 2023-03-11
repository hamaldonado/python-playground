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
    t.speed(1000)
    turtle.bgcolor("black")

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    finish = 343
    stop = int(finish / len(colors))  #50

    for i in range(5, finish, 3):

        color_idx = len(colors) - int(i / stop) - 1

        t.pencolor(colors[color_idx])
        
        draw_figure(5, i)
        t.rt(10)
        
main()

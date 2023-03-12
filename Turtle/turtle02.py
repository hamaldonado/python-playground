import turtle

c = turtle.Screen()
t = turtle.Turtle()


def draw_figure(side_count, side_size):
    angle = int(360 / side_count)

    #t.lt(90)

    for i in range(0, side_count):
        t.fd(side_size)
        t.rt(angle)

def draw_wheel():

    for i in range(0, 45):
        draw_figure(3, 100)
        t.lt(8)
        

def draw_snail():
    turtle.bgcolor("black")
    t.pencolor("yellow")

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    finish = 343
    stop = int(finish / len(colors))  #50

    for i in range(5, finish, 3):

        color_idx = len(colors) - int(i / stop) - 1

        t.pencolor(colors[color_idx])
        
        draw_figure(5, i)
        t.rt(10)


def main():
    t.speed(1000)
    

    draw_wheel()
            
main()

"""Paint, for drawing shapes.

Exercises

1. Add a color. (OK)
2. Complete circle. (OK)
3. Complete rectangle. (OK)
4. Complete triangle. (OK)
5. Add width parameter. (no)
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end): # (2. Complete circle)
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    import turtle # (Importando a biblioteca turtle dentro da função)
    
    turtle.speed(0)
    turtle.circle(start.x - end.x) 

    end_fill()



def rectangle(start, end): # (3. Complete circle)
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    width = start.x - end.x
    for count in range(2):
        forward(width)
        left(90)
        forward(width-(width/3))
        left(90) 

    end_fill()


def triangle(start, end): # (4. Complete triangle)
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = start.x - end.x
    for count in range(3):
        forward(width)
        right(360/3)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('orange'), 'O') # (1. Add a color)
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

from turtle import *
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
            left(val)
    elif do == 'U':
            penup()
    elif do == 'D':
            pendown()
    elif do == 'N':
            reset()
    else:
            print('Unrecorgnized command')
turtle_controller('F', 100)
turtle_controller('R', 90)
turtle_controller('F', 50)


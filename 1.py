''';ppppppppppp;ppppppppppppppioo900000|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?|?OI{}<
Created on 10 мар. 2025 г.

@author: Kabirov Kamil
'''

import turtle
def kv():
        turtle.forward(100)                               
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

def Squere(X, Y, a, b):
#    turtle.up()
#    turtle.forward(dX)
    turtle.teleport(X, Y)
    turtle.seth(0)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    
Squere(0, 0 , 10 , 20)
Squere(40, 0 , 10 , 20)
Squere(80, 0 , 10 , 20)
Squere(120, 0 , 10 , 20)

turtle.exitonclick()

    
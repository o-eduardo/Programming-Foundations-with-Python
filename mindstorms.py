import turtle 
def draw_art():
    #desenha quadrado
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(0)
    brad.width(3)
    brad.color("purple")
    
    bill = turtle.Turtle()
    bill.shape("arrow")
    bill.speed(5)
    bill.width(1)
    bill.color("pink")

    
    draw_squarC(brad,bill, 100)
    #draw_squarC(bill, 100)
    

    window.exitonclick()

def draw_square(some_turtle, side):
    for i in range(1,5):
        some_turtle.forward(side)
        some_turtle.right(90)


def draw_squarC (some_turtle1,some_turtle2,side):
    for i in range (0,36):
        draw_circle(some_turtle1, side)
        some_turtle1.right(10)
        for j in range (0, 10):
            draw_triangle(some_turtle1,side)
            some_turtle1.left(36)
            
    else:
        some_turtle2.left(90)
        some_turtle2.forward(2*side)

    
    
def draw_circle(some_turtle, radius):
    some_turtle.circle(radius)


def draw_triangle(some_turtle, side):
    for i in range(1,4):
        some_turtle.forward(side)
        some_turtle.left(120)
        
 

draw_art()

#tornar draw_square(side) iterativo
#criar draw_circle(radius)
#criar draw+triangle(side) -->chega side  --> convrete para radiano ->calcula tudo --> converte para degree

import turtle
t = turtle.Turtle()
t.speed(1.3)

def draw_J():
    t.penup()
    t.goto(-80, 0)
    t.pendown()
    t.color("red")
    t.width(5)
        
    t.left(90)
    
    t.right(90)
    t.backward(60)
        
    t.forward(100)
    
    t.right(90)
    t.forward(20)
    
    t.right(90)
    t.backward(-35)
    
    t.right(90)
    t.backward(100)
    
    t.left(90)
    t.forward(80)
    
    t.right(90)
    t.forward(40)
    
    t.left(90)
    t.backward(20)
    
    t.right(90)
    t.backward(25)
    
    t.right(90)
    t.forward(30)
    
    t.left(90)
    t.forward(85)
    
    t.left(90)
    t.forward(40)
    
    t.right(90)
    t.forward(20)
    
    t.right(90)
    t.forward(10) 
# Main function
def main():
    turtle.bgcolor("black")
    draw_J()
    turtle.done()

if __name__ == "__main__":
    main()

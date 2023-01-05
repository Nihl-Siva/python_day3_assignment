from math import pi

def area_calc():
    
    while True:
        side1 = float(input("What is the length of the first side?: "))
        if side1 > 0:
            side2 = float(input("What is the width of the second side?: "))
            print(f"The area of the room is {side1*side2}.")
            break
            
    

def circ_calc():

    while True:
        radius = float(input("What is the radius of the circle?: "))
        if radius > 0:
            print(f"The circumference of the circle is {radius*2*pi}.")
            break

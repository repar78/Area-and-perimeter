print(" welcome \n Please select \n")
print(" 1.Rectangle \n 2.Square \n 3.triangle")
number =int(input("\n number:"))

if number == 1:
    length = float(input("Enter the length of the rectangle:"))
    width  = float(input("Enter the width of the rectangle :"))
    print (f"area={length*width}")
    print(f"Perimeter  ={(length+width) * 2}")   
    
elif number == 2:
    side   = float(input("Write the size of the side of the square :"))
    print(f"area={side*side}")
    print(f"Perimeter  ={(side * 4)}")  
    
else:
    base   = float(input("Enter the base of the triangle:"))
    Height = float(input("Write the height of the triangle:"))
    print(f"area={base*height}")


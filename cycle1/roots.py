print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
print("Equation: ax^2 + bx + c ")
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
d = b**2-4*a*c
dl = d**0.5
if d < 0:
    print("the roots are imaginary")
else:
    r1 = (-b + dl) / 2 * a
    r2 = (-b - dl) / 2 * a
    print("the first root:", round(r1, 2))
    print("the second root:", round(r2, 2))




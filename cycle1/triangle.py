print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
print("Input lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
    print("It is an Equilateral triangle")
elif a == b or b == c or c == a:
    print("It is an Isosceles triangle")
else:
    print("It is a Scalene triangle")

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
num = int(input("enter limit:"))
n1, n2 = 0, 1
for i in range(0, num):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3


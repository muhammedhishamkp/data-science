print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
def are_coprime(a, b):
    hcf = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf == 1
first = int(input("enter first number:"))
second = int(input("enter first number:"))
if are_coprime(first, second):
    print("%d and %d are coprime" % (first, second))
else:
    print("%d and %d are not coprime" % (first, second))

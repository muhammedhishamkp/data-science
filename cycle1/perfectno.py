print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
num = int(input("enter a number:"))
sum = 0
for i in range(1, num):
    if (num % i == 0):
        sum = sum + i
if (sum == num):
    print("the enterd number is perfect number")
else:
    print("the enterd number is not a perfect number")
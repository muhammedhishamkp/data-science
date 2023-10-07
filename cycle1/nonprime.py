print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
u = int(input("enter lower limit:"))
v = int(input("enter upper limit:"))
print("prime numbers between",u,"and",v,"are:")
for i in range(u, v + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                print(i)
                break


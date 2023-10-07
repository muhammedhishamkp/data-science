print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
print("armstrong numbers upto 1000 are:")
for num in range(1, 1001):
    num_digit = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum +=digit ** num_digit
        temp //=10
    if num == sum:
        print(num)

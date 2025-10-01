num = int(input("Enter a number: "))
if num <= 0:
    print("No")
else:
    while num % 8 == 0:
        num = num // 8
    print("Yes, it is the power of 8" if num == 1 else "Not the power of 8")

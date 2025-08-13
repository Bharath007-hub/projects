a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
small = min(a, b)
large = max(a, b)
i = large
while True:
    if i % small == 0 and i % large == 0:
        print("LCM is", i)
        break
    i += 1

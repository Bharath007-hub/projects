start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if 10 <= num <= 99 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        print(num)

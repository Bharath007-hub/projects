def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_binary(d):
    return bin(d)[2:]

choice = input("Convert (1) Binary to Decimal or (2) Decimal to Binary: ")

if choice == "1":
    b = input("Enter binary number: ")
    print(binary_to_decimal(b))
elif choice == "2":
    d = int(input("Enter decimal number: "))
    print(decimal_to_binary(d))

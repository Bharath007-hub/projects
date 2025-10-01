def find_first_set_bit_position(num):
    if num == 0:
        return 0  
    position = 1  
    while num & 1 == 0:
        num = num >> 1
        position += 1
    return position

try:
    number = int(input("Enter a number: "))
    position = find_first_set_bit_position(number)
    if position == 0:
        print("No set bits found in the number.")
    else:
        print(f"The position of the first set bit is: {position}")
except ValueError:
    print("Please enter a valid integer.")

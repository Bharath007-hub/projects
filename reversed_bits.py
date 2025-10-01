num = int(input("Enter a number: "))
bit_length = num.bit_length()
reversed_bits = 0
for i in range(bit_length):
    if (num >> i) & 1:
        reversed_bits |= 1 << (bit_length - 1 - i)

print("Original number:", num, f"({format(num, f'0{bit_length}b')})")
print("Reversed number:", reversed_bits, f"({format(reversed_bits, f'0{bit_length}b')})")

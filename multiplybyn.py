def multiply(n, m):
    return iterate_addition(n, m)

def iterate_addition(n, m):
    result = 0
    for _ in range(n):
        result += m
    return result

print(multiply(5, 3))

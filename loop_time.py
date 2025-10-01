def myfunction(n):
    print("Running First Loop:")
    for i in range(0, n + 1):
        print("First Loop")  # O(n)

    print("Running Second Loop:")
    j = 1
    while j <= n + 1:
        print("Second Loop", j)  # O(log n)
        j = j * 2

    print("Running Third Loop:")
    for i in range(0, 100):
        print("Third Loop")  # O(1)

    print("\nTime Complexities:")
    print("First Loop: O(n)")
    print("Second Loop: O(log n)")
    print("Third Loop: O(1)")
    print("Total Time Complexity: O(n)")  # Dominant term


# Example usage:
myfunction(10)

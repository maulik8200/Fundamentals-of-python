def generate_fibonacci(n):
    fib = [0, 1]

    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])

    return fib

range_limit = int(input("Enter the range limit: "))

fibonacci = generate_fibonacci(range_limit)
print(f"Fibonacci series within the range up to {range_limit}:")
print(fibonacci)
def sum_of_positive_integers(n):
    if type(n) == int and n > 0:
        sum_result = (n * (n + 1))
        return sum_result
    else:
        print("Please enter a positive integer.")

n = int(input("Enter a positive integer (n): "))

result = sum_of_positive_integers(n)
if result is not None:
    print(f"The sum of the first {n} positive integers is: {result}")
def sum_of_three_integers(a, b, c):
    if a == b or b == c or a == c:
        result = 0
    else:
        result = a + b + c

    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result_sum = sum_of_three_integers(num1, num2, num3)
print(f"The sum of the three number is: {result_sum}")
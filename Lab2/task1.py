n = int(input("Please enter a positive integer greater than 9: "))

steps = 0
while n > 9:
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    n = sum_digits
    steps += 1
    print(n, end=" : " if n > 9 else "\n")

print(f"Final value: {n}")
print(f"Total steps: {steps}")

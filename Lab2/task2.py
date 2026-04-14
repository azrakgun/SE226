
n = int(input("Please enter a number between 10 and 100: "))
while n < 10 or n > 100:
    n = int(input("Invalid input. Please enter a number between 10 and 100: "))

fizz = buzz = fizzbuzz = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz += 1
    else:
        print(i)

# Özet
print("- Summary -")

print(f"Fizz count : {fizz}")
print(f"Buzz count : {buzz}")
print(f"FizzBuzz count: {fizzbuzz}")

def factorial (x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def exp_x(x, n):

    absolute_val = lambda val: val if val >= 0 else val * - 1

    total_sum = 0
    for i in range(n):
        ust = x ** (2 * i)
        alt = factorial(2 * i)
        term = ust / alt

        if i % 2 == 0:

            total_sum += absolute_val(term)

        else:

            total_sum -= absolute_val(term)

        return total_sum

x_value = float( input("X : "))
n_value = int(input(" (n) "))

final_value = exp_x(x_value, n_value)
print(" : " , final_value)




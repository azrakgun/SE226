gn_sum = 0

def calculate_gn(n, r):

    """The function takes "n" (number of terms) and "r" (common ratio) as parameters but returns nothing"""

    global gn_sum

    if n < 0:
        return
    gn_sum += r ** n
    calculate_gn(n-1, r)


n = 5
r = 7

calculate_gn(n, r)
print(gn_sum)










def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10

    return total == n

print(is_armstrong(153))

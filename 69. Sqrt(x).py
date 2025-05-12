def sqrt_floor(x):
    if x == 0:
        return 0
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    return guess

print(sqrt_floor(10))  # Output: 3
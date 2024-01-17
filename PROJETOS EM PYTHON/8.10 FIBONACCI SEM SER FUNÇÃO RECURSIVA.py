def fibonacci(n):
    x1 = -1
    x2 = 1
    y = 0
    while y <= n:
        x = x1 + x2
        print(f"{x}", end=" ")
        y += 1
        x1 = x2
        x2 = x
fibonacci(5)
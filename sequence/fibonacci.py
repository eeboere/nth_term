def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def find_fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(1, n):
        curr_fib = fib1 + fib2
        fib1 = fib2
        fib2 = curr_fib
    return fib2


if __name__ == '__main__':
    print(find_fibonacci(3))  # 2
    print(find_fibonacci(4))  # 3
    print(find_fibonacci(5))  # 5
    print(find_fibonacci(6))  # 8

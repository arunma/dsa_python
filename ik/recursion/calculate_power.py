def calculate_power(a, b):
    if b == 0:
        return 1
    if b & 1:
        return a * calculate_power(a * a, b // 2)
    else:
        return calculate_power(a * a, b // 2)


# def binaryExp(x: float, n: int) -> float:
#     # Base case, to stop recursive calls.
#     if n == 0:
#         return 1
#
#     # Handle case where, n < 0.
#     if n < 0:
#         return 1.0 / binaryExp(x, -1 * n)
#
#     # Perform Binary Exponentiation.
#     # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
#     if n % 2 == 1:
#         return x * binaryExp(x * x, (n - 1) // 2)
#     # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
#     else:
#         return binaryExp(x * x, n // 2)


# def calculate_power(a, b):
#     result = 1
#     while b:
#         if b & 1:
#             result *= a
#         a *= a
#         b //= 2
#     return result


#
# def calculate_power(a, b):
#     pwr = a
#     for i in range(1, b):
#         pwr *= a
#     return pwr


if __name__ == '__main__':
    # print(calculate_power(2, 10))
    # print(calculate_power(2, 2))
    # print(calculate_power(2, 4))
    # print(calculate_power(2, 7))
    print(calculate_power(2, 32))  # 294967268
    # print(binaryExp(2, 32))  # 294967268

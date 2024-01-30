def decimal_to_binary(n):
    binary = ""
    while n != 0:
        binary += str(n % 2)
        n = n // 2
    return binary[::-1]

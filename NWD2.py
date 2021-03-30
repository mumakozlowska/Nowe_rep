def nwd(a, b):
    while b != 0:
        a, b = b, a
        b = a % b

        return b

def euclid(m, n):
    r = m % n
    if r == 0:
        return n
    return euclid(n, r)


if __name__ == '__main__':
    greatest_common_divisor = euclid(42, 12)
    print(greatest_common_divisor)

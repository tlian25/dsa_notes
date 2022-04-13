# Greatest Common Divisor and Least Common Multiple

from functools import reduce

def gcd(a:int, b:int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


def gcd_list(lst: list) -> int:
    return reduce(gcd, lst)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def lcm_list(lst: list) -> int:
    return reduce(lcm, lst)



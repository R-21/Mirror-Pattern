"""
Author: Krish Rogan
Date: 13-07-2023
Dependency: n value should be 2 to 9 to generate a good visual pattern
"""
from math import ceil

global x
global concrete
global n


def convert_to_int(pat):
    """

    :param pat: generated list of strings pattern
    """
    return [int(p_) for p_ in pat]


def set_(n_):
    """
    :param n_: number of rows
    """

    global x, concrete, n
    n = n_ * 2
    x = ceil(n / 2)
    concrete = ''.join(map(str, range(1, x+1)))


def mirror(p1: (list, tuple)):
    """
    :param p1: must be list or tuple
    :return: reverse of the p1, without the last index
    """
    return p1[:-1][::-1]


def get_concrete(o):
    """
    :param o: represent nth index
    :return: side pattern
    """
    return concrete[x - o:x]


def create_side_wall(o, r):
    """
    :param o: represent nth row
    :param r: reverse or not
    :return: Left or right side wall pattern
    """
    return get_concrete(o)[::-1] if r == 0 else get_concrete(o)


def create_inner_wall(u, o):
    """
    :param u: number of rows - current row index
    :param o: represent nth index
    :return: inner structure of pattern
    """
    return str(x - o) * (u - o)


def make_wall(o):
    """
    :param o: represent nth row
    :return: single row pattern
    """
    return create_side_wall(o, 0) + create_inner_wall(n - o, o) + create_side_wall(o, 1)


def make_pattern(n_):
    """
    :param n_: number of rows
    :return: list of strings
    """
    set_(n_)
    half_pat = [make_wall(e) for e in range(x)]
    return half_pat + mirror(half_pat)


if __name__ == '__main__':
    n = 5
    pattern = make_pattern(n)
    for p in pattern:
        print(p)

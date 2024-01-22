#!/usr/bin/python3
"""Defines the minoperations function"""


def minOperations(n):
    if n <= 1:
        return 0

    ops = 0
    div = 2

    while n > 1:
        while n % div == 0:
            ops += div
            n //= div
        div += 1

    return ops

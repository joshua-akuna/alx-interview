#!/usr/bin/env python3

def validUTF8(data):
    start_mask = [128, 192, 224, 240]

    i = 0
    while i < len(data):
        count_ones = 0
        while i < len(data) and (data[i] & 128) == 128:
            count_ones += 1
            data[i] = data[i] << 1 & 255

        if count_ones == 1 or count_ones > 4 or (
                count_ones > 0 and i == len(data) - 1):
            return False

        if count_ones > 1:
            for j in range(1, count_ones):
                if i + j >= len(data) or (data[i + j] & 192) != 128:
                    return False

        i += count_ones + 1

    return True

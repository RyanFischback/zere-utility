"""
Author: Ryan Fischback
Date: 2024-08-01

Description:
    This script processes input numbers based on a threshold and limit,
    and outputs the results. It reads up to 100 lines of input, performs
    calculations, and prints the results along with the limit.
"""

import argparse

def process(threshold: float, limit: float):
    total = 0.0
    max_lines = 100
    results = []

    try:
        for _ in range(max_lines):
            line = input().strip()
            if line == "":
                break

            try:
                number = float(line)
            except ValueError:
                continue 

            if number > threshold:
                value = min(number - threshold, limit - total)
                results.append(value)
                total += value
            else:
                results.append(0.0)
    except EOFError:
        pass
            
    return results, total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('threshold', type=float)
    parser.add_argument('limit', type=float)
    args = parser.parse_args()
    threshold = args.threshold
    limit = args.limit
    results, total = process(threshold, limit)
    if results:
        print('\n'.join(map(str, results)))
    print(total, end='')
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    matrix = []
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            matrix.append([int(x) for x in line.split()])
    return matrix

def is_report_safe(level):
    is_ascending = level[0] <= level[1]
    for i in range(len(level)-1):
        diff = level[i+1] - level[i]
        if ((diff > 0 and not is_ascending) or (diff <= 0 and is_ascending)):
            return 0
        diff = abs(diff)
        if diff < 1 or diff > 3:
            return 0
    return 1

def count_safe_levels(matrix, extra_safety):
    nb_safe_levels = 0
    for report in matrix:
        is_safe = is_report_safe(report)
        if (not is_safe):
            for i in range(len(report)):
                if (is_report_safe(report[:i] + report[i+1:])):
                    nb_safe_levels += 1
                    break
        nb_safe_levels += is_safe
    return nb_safe_levels

if __name__ == '__main__':
    args = parse_args()
    matrix = parse_input(args.input)
    nb_safe_levels = count_safe_levels(matrix, 1)
    print(nb_safe_levels)
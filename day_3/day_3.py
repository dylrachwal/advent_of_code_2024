import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def search_pattern(input):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    res = re.findall(pattern, input)
    return res

def compute_mul(strings):
    res = 0
    do = True
    for value in strings:
        if (value == 'do()'):
            do = True
        elif (value == 'don\'t()'):
            do = False
        else:
            x,y=value[4:-1].split(',')
            res += int(x) * int(y) if do else 0
    return res

if __name__ == '__main__':
    args = parse_args()
    input = open(args.input).read()
    res = search_pattern(input)
    print(compute_mul(res))
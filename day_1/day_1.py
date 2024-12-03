import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    left, right = [], []
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.split()
            left.append(int(a))
            right.append(int(b))
    return left, right

def calc_distance(left, right):
    left.sort()
    right.sort()
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i]- right[i])
    return distance

def calc_similarity(left, right):
    similarity = 0
    for value in left:
        similarity += value * right.count(value)
    return similarity

if __name__ == '__main__':
    args = parse_args()
    left, right = parse_input(args.input)
    distance = calc_distance(left, right)
    print(f"distance : {distance}")
    similarity = calc_similarity(left, right)
    print(f"similarity: {similarity}")
